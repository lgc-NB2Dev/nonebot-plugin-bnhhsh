from nonebot import get_driver
from pydantic import BaseModel


class Cfg(BaseModel):
    bnhhsh_unv_mse: float = 0.2


config: Cfg = Cfg.parse_obj(get_driver().config.dict())
