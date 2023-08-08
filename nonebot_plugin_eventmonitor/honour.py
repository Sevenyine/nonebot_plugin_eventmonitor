from .utils import superusers


async def monitor_rongyu(honor_type, user_id, bot_qq):
    rely = ""  
    # 根据honor_type选择不同的消息
    if honor_type == "emotion":
        # 如果用户ID等于机器人的QQ号，不作任何操作
        if user_id == bot_qq:
            rely = "你们又不行了，本咕喜提快乐源泉~"
        # 如果用户ID在superusers列表中，返回特定消息
        elif user_id in superusers:
            rely = f"恭喜QQ={user_id}荣获快乐源泉标识~"
        # 否则，返回通用消息
        else:
            rely = f"恭喜QQ={user_id}荣获快乐源泉标识~"
            
    elif honor_type == "performer":
        # 如果用户ID等于机器人的QQ号，不作任何操作
        if user_id == bot_qq:
            rely = "你们又不行了，本喵喜提群聊之火🔥~"
        # 如果用户ID在superusers列表中，返回特定消息
        elif user_id in superusers:
            rely = f"恭喜qq={user_id}获群聊之火🔥标识(^з^)-☆"
        else:
            rely = f"恭喜qq={user_id}获群聊之火🔥标识(^з^)-☆"

    elif honor_type == "talkative":
        # 如果用户ID等于机器人的QQ号，返回特定消息
        if user_id == bot_qq:
            rely = "你们又不行了，本鸽子都能喜提龙王╮(￣▽￣"")╭"
        elif user_id in superusers:
            rely = f"恭喜qq={user_id}获龙王🐲标识(*≧ω≦)"
        else:
            rely = f"恭喜qq={user_id}获龙王🐲标识(*≧ω≦)"

    return rely

