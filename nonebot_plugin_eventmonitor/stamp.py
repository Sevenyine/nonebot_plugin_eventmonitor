import random
from .utils import nickname


async def chuo_send_msg():
    # 使用 random.randint() 生成一个随机整数，作为选择消息的索引
    rand_num = random.randint(0, len(chuo_msg) - 1)  
    # 返回位于随机索引处的消息
    return chuo_msg[rand_num]

#戳一戳文案
chuo_msg = [
    #卖萌
    f"别戳了，{nickname}怕疼QwQ",
    f"呜呜，再戳{nickname}脸都要肿了",
    f"戳坏了{nickname}，你赔得起吗？",
    f"再戳{nickname}，我要叫我主人了",
    f"别老戳{nickname}了，您歇会吧~",
    f"再戳{nickname}，咬你了嗷~",
    f"想好了再戳，(*-`ω´-)✄",
    f"嗷呜嗷呜...恶龙咆哮┗|｀O′|┛",
    f"有事恁叫我，别天天一个劲戳戳戳！",
    f"再戳我让你变成女人，嘿嘿",
    f"咱要型气了o(>﹏<)o",
    f"你不会是在这里消遣鸽子吧！",
    f"嘿嘿，好舒服呀(bushi)",
    f"Σ(￣。￣ﾉ)ﾉ",
    f"(///▽///)",
    f"(。´・ω・)ん?",
    #真实
    f"喂，110吗，有人老戳我",
    f"正在定位您的真实地址...定位成功。轰炸机已起飞",
    f"再戳，小心我顺着网线找你",
    #劝停
    f"一寸光阴一寸金，不戳鸽子省光阴",
    f"不要戳我了 >_<",
    f"不要这样子啦(*/ω＼*)",
    f"不要再戳了(害怕ing)",
    f"还戳，哼(つд⊂)（生气）",
    f"lsp你再戳？",
    f"别再戳我了，行🐎？！",
    f"我爪巴爪巴，球球别再戳了",
    f"你再戳！",
    f"？再戳试试？",
    f"别戳了别戳了再戳就坏了555",
    f"我爪巴爪巴，球球别再戳了",
    f"乖，好了好了，别戳了~",
    f"你戳你🐎呢？！",
    f"请不要戳{nickname}啦 >_<",
    f"放手啦，不给戳QAQ",
    f"喂(#`O′) 戳{nickname}干嘛！",
    f"有事恁叫我，别天天一个劲戳戳戳！",
    f"再戳一下试试？",
    f"闲的没事去玩漂流瓶吧",
    #正经
    f"啊呜，你有什么事吗？",
    f"我不是戳戳回复bot！",
    #发癫
    f"每次都想装作很倔强～但是见面自己却缴械投降～",
    f"我实在想不出来了，这个凑数应该没人发现吧",
    #坏了
    f"戳坏了，赔钱！",
    f"戳坏了。哔哔。",
    f"嗯……不可以……啦……不要乱戳",
    f"那...那里...那里不能戳...绝对...",
    f"哔哔，啵啵，哔哔？",
    f"戳坏了，智商-1",
    f"啊吧啊吧",
    f"[FATAL] httpx.ReadTimeout",
    f"ssl.SSLWantReadError: The operation did not complete (read) (_ssl.c:2548)",
    f"我是一头好人啊，不是不是我是一匹村民",
    f"啊对的对的，啊不对不对",
    f"啊呜，太舒服刚刚竟然睡着了。什么事？",
    f"正在关闭对您的所有服务...关闭成功",
    #骂人
    f"谁再戳谁烧0",
    f"欸很烦欸！你戳🔨呢",
    f"你们没有自己的事情要干嘛！！",
    f"再戳？再戳鸽了你。",
    #梗
    f"v我50",
    #冷知识
    f"你说的对，但是bot的戳一戳cd是8秒",
    #公式
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？T^2=frac(4pi^2 r^3)(MG)",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？x^(prime)=frac(x-v t)(sqrt(1-frac(v^2)(c^2)))",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？t^(prime)=frac(t-frac(v)(c^2) x)(sqrt(1-frac(v^2)(c^2)))",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？dL=dl/γ",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？dt=dτ/γ",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？E=mc^2",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？Co + 2Fe == CoFFee",
    f"刚刚被戳傻了，脑子里突然出现了一个公式，你知道这是什么吗？Mn + O2 == MOOn",
    #冷笑话
    f"猜猜为什么苹果专卖店里不能放屁？因为里面没有windows。",
    f"为什么电脑经常生病？因为它的窗户（Windows）总是开着。",
    f"小明建房子没钱打地基了，他灵机一动搬来一堆荆棘，请问为什么？因为荆棘基础决定上层建筑。",
    f"诸葛亮对风说，风啊你快向西刮吧。风说：你**才像西瓜。",
    f"一只鲨鱼被迷倒了之后拍的照片叫什么？答：婚纱照（昏鲨照）。",
    f"一根牙签走在路上看见了一只刺猬，它停下来招手说：诶公交车等等我！",
    f"有一群小动物聚餐，只有一只小象特别生气，请问他们在哪？答：气象局。这个笑话是把小象生气缩写成气象，再通过气象这两个字可以对应地名：气象局来营造一种幽默的氛围。",
    f"愚公移山的时候最喜欢唱的歌是什么歌？答：移山移山（一闪一闪）亮晶晶。不好笑吗？",
    f"“A girl phoned me the other day and said “Come on over, there’s nobody home.” I went over. Nobody was home.” – Rodney Dangerfield",
    f"一位大妈坐在江边对着江水痛哭 “我的孩子啊！……” 一位热心小哥看见赶紧冲过来问完 “你孩子在哪儿？” 就跳进江里了，过了十分钟，小哥很沮丧地爬上岸跟大妈说 “非常抱歉，你的孩子我没捞起来，找了半天只捞到他的一只鞋子”。这个笑话是部分方言把鞋子发音为孩子，导致了误解。",
    f"让我们做些关上灯才能做的事情吧。比如说：开灯。",
    f"红苹果(🍎)，青苹果(🍏)，红梨子(🍐)，氢离子(H+)",
    f"开水放凉了叫什么？答：白开水。因为放凉了的开水“白开”了。",
    f"医生对一个病人说，你的身体缺镁。请问病人会说什么？答：0Mg。因为Mg是镁的化学符号，而0代表没有。同时，0Mg和Omg非常像，也表达了病人的惊讶之情。",
    f"一只鳄鱼睡着了，请问他做的梦叫什么梦？答：噩（鳄）梦。",
    f"有一天，小明忘记带钥匙了，请问他会去哪？答：去研究所（研究锁）。",
    f"有一天小明下楼扔垃圾，阿姨问：你这是垃圾吗？小明：不是，是干垃圾。这个笑话的笑点在于，是垃圾和湿垃圾的发音相似，导致小明误以为在问垃圾的种类。",
    f"小明每天都用自己的巴掌叫醒自己，请问为什么？答：吾日扇醒（三省）吾身。",
    f"请问枇杷做成的面叫什么？答：油爆枇杷拌着面。",
    f"按时上班有全勤奖，那按时下班有什么奖？答：老板有话奖（讲）。",
    f"老王吃花椒，打一歇后语。答：麻了**",
    f"为什么理发店老师出门要带水？答：tony（拖泥）带水。",
    f"一个少年吃了同学，应该叫他什么？答：恰同学少年。",
    f"有人考了1分。应该叫他什么？答：思国一（score 1）。",
    f"白气球把黑气球打了一顿，所以黑气球决定：告白气球。",
    f"一条鱼在太阳底下快被晒死了，临死前对另一条鱼说：兄弟啊我干了哈你随意。",
    f"为什么蚕宝宝很有钱？因为他会结茧（节俭）。",
    f"猴子不喜欢什么线？答：平行线，因为平行线没有相交（香蕉）",
    f"林黛玉是怎么死的？答：摔死的，因为天上掉下个林妹妹",
    f"什么动物喜欢贴在墙上？答：海豹（报）",
    f"更多冷笑话，尝试捡捡漂流瓶吧～"
]
