from nonebot.plugin import PluginMetadata

from .__main__ import *

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="「不能好好说话！」",
    description="不对劲的拼音首字母缩写翻译工具",
    usage="直接发送纯英文消息，插件会自动帮你翻译缩写",
    extra={
        "version": __version__,
        "license": "MIT",
        "author": "student_2333 <lgc2333@126.com>",
    },
)
