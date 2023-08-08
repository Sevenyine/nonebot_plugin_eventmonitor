from datetime import datetime
from .utils import superusers


async def admin_changer(sub_type, user_id, bot_qq) :
    admin_msg = ""
    
    # 根据管理员变动类型选择不同的消息
    if sub_type == "set":
        # 如果用户ID等于机器人的QQ号，返回特定消息
        admin_msg = (
            "鸽子也是管理啦~可以用鸽子群管功能啦(｡･ω･｡)"
            if user_id == bot_qq
            else f"🚔 管理员变动\n恭喜QQ={user_id}喜提本群管理~"
        )
    elif sub_type == "unset":
        # 如果用户ID等于机器人的QQ号，返回特定消息
        admin_msg = (
            "呜呜，鸽子被下管理了(´･_･`)，咕咕呜"
            if user_id == bot_qq
            else f"🚔 管理员变动\nQQ={user_id}痛失本群管理∑(ﾟДﾟ)"
        )
        
    return admin_msg


async def del_user_bye(add_time, user_id):
    global del_user_msg
    del_time = datetime.fromtimestamp(add_time)
    
    # 检查用户ID是否在超级用户列表superusers中
    if user_id in superusers:
        # 如果是超级用户，生成特定的离开消息
        del_user_msg = f"⌈{del_time}⌋\n@{user_id}恭送主人离开喵~"
    else:
        del_user_msg = f"✈️ 成员变动⌈{del_time}⌋\nQQ号为：{user_id}的小可爱退群/被踢出群聊喽~" \
                       f"[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={user_id}&spec=640]"
                       
        return del_user_msg


async def add_user_wecome(add_time, user_id, bot_qq):
    global groups_all, add_user_msg   
    # 将时间戳转换为datetime类型的时间add_time
    add_time = datetime.fromtimestamp(add_time) 
    # 判断用户ID是否等于机器人的QQ号
    if user_id == bot_qq:
        add_user_msg = f"本鸽被邀进入贵群~\n" \
                       f"火速上个管理咕咕咕"
    elif user_id in superusers:
        add_user_msg = f"✨ 成员变动 ✨\n欢迎QQ={user_id}的加入~\n加入时间：⌈{add_time}⌋"
    else:
        add_user_msg = f"✨ 成员变动 ✨\n欢迎QQ={user_id}的加入~\n加入时间：⌈{add_time}⌋"
    return add_user_msg

