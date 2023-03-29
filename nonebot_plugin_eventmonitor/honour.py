import nonebot
from nonebot.permission import SUPERUSER

try:
    bot_qq = nonebot.get_driver().config.bot_qq
except:
    bot_qq = "寄"

try:
    super_qq = nonebot.get_driver().config.superusers
except:
    super_qq = "寄"


def monitor_rongyu(honor_type, user_id):
    rely = ""

    if honor_type == "talkative":
        if user_id == bot_qq:
            rely = f"你们又不行了，本鸽子都能喜提龙王╮(￣▽￣"")╭"
        elif user_id == super_qq:
            rely = f"恭喜qq={user_id}获龙王🐲标识(*≧ω≦)"
        else:
            rely = f"恭喜qq={user_id}获龙王🐲标识(*≧ω≦)"

    elif honor_type == "performer":
        if user_id == bot_qq:
            pass
        elif user_id == super_qq:
            rely = f"恭喜qq={user_id}获群聊之火🔥标识(^з^)-☆"
        else:
            rely = f"恭喜qq={user_id}获群聊之火🔥标识(^з^)-☆"

    elif honor_type == "emotion":
        if user_id == bot_qq:
            pass
        elif user_id == super_qq:
            rely = f"恭喜qq={user_id}获快乐源泉标识(*≧ω≦)"
        else:
            rely = f"恭喜qq={user_id}获快乐源泉标识(*≧ω≦)"
    return rely
