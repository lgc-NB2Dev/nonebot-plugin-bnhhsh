from nonebot import logger, on_regex
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from unvcode import unvcode

from .bnhhsh.bnhhsh import dp
from .config import config

matcher = on_regex(r"^[a-zA-Z\s]+$")


def str_to_hex(s):
    return f"0x{s.encode('utf-8').hex()}"


@matcher.handle()
async def _(event: MessageEvent):
    def f_hex(x):
        return f"{(x)}({str_to_hex(x)})"

    translated = {}
    for w in event.message.extract_plain_text().split():
        if not w:
            continue

        w = w.lower()
        if w.isalpha():
            origin = dp(w)
            result, mse = unvcode(origin, mse=config.bnhhsh_unv_mse)
            translated[w] = result

            for l in [
                f"替换 {f_hex(origin[i])} -> {f_hex(result[i])} ({100 - x * 100:.2f}% 相似)"
                for i, x in enumerate(mse)
                if x is not None
            ]:
                logger.info(l)

    if translated:
        await matcher.finish(
            MessageSegment.reply(event.message_id)
            + "\n".join([f"{k}: {v}" for k, v in translated.items()])
        )
