from .bnhhsh.bnhhsh import dp
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment

matcher = on_regex(r"[a-zA-Z\s]+")


@matcher.handle()
async def _(event: MessageEvent):
    translated = {}
    for w in event.message.extract_plain_text().split():
        if not w:
            continue

        w = w.lower()
        if w.isalpha():
            translated[w] = dp(w)

    if translated:
        await matcher.finish(
            MessageSegment.reply(event.message_id)
            + "\n".join([f"{k}: {v}" for k, v in translated.items()])
        )
