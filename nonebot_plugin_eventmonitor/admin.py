from datetime import datetime
from .honour import bot_qq, super_qq



def admin_changer(sub_type, user_id):
    admin_msg = ""
    if sub_type == "set":
        if user_id == bot_qq:
            admin_msg = f"鸽子也是管理啦~可以用鸽子群管功能啦(｡･ω･｡)"
        else:
            admin_msg = f"🚔 管理员变动\n恭喜QQ={user_id}喜提本群管理~"
    elif sub_type == "unset":
        if user_id == bot_qq:
            admin_msg = f"呜呜，鸽子被下管理了(´･_･`)，咕咕呜~"
        else:
            admin_msg = f"🚔 管理员变动\n[CQ:at,qq={user_id}]痛失本群管理∑(ﾟДﾟ)"
    return admin_msg


def del_user_bye(add_time, group_id, user_id):
    global groups_all, del_user_msg
    del_time = datetime.fromtimestamp(add_time)
    if user_id in super_qq:
        del_user_msg = f"⌈{del_time}⌋\n@{user_id}恭送主人离开喵~"
    else:
        del_user_msg = f"✈️ 成员变动⌈{del_time}⌋\nQQ号为：{user_id}的小可爱退群喽~" \
                       f"[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={user_id}&spec=640]"
        return del_user_msg


def add_user_wecome(add_time, group_id, user_id):
    global groups_all, add_user_msg
    add_time = datetime.fromtimestamp(add_time)
    if user_id == bot_qq:
        add_user_msg = f"本鸽被邀进入贵群喵~\n" \
                       f"好好用本bot哦~"
    else:
        add_user_msg = f"✨ 成员变动 ✨\n欢迎QQ={user_id}]的加入~\n加入时间：⌈{add_time}⌋"
    return add_user_msg
