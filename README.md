<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>


<div align="center">
# Monitor_Groups

_✨ 基于NoneBot2实现的 监测QQ群事件 插件 ✨_

</div>

# 自用 修改了部分口头禅



## 介绍：
> 监测群组的以下变动事件：
>
> 群成员增加、减少时，自动发送通知
>
> 群管理变更时，自动发送通知
>
> 被其他成员戳一戳时，自动回复
>
> 群成员上传文件时，自动发送通知
>
> 群红包被抢完时，自动发送红包运气王
>
> 群成员荣誉变更时，发送变更通知

## 安装方式

### nb-cli安装(推荐)

```
nb plugin install nonebot_plugin_eventmonitor
```

<details><summary><h3>pip</h3></summary>


```
pip install nonebot-plugin-eventmonitor
```
打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin("nonebot_plugin_eventmonitor")

在’pyproject.toml‘文件中写入

    "nonebot_plugin_eventmonitor"

</details>

<details><summary><h3>git clone</h3></summary>

```
git clone https://github.com/Reversedeer/nonebot_piugin_eventmonitor.git
```

</details>

### 更新

```
pip install --upgrade nonebot-plugin-eventmonitor
```

## 配置

在bot目录对应的.env.*文件中添加（SUPERUSERS应该都填了吧）

|   config   | type | default |         example          |                    usage                    |
| :--------: | :--: | :-----: | :----------------------: | :-----------------------------------------: |
|   bot_qq   | int  |   寄    |    bot_qq = 123456789    |    bot群聊变动和群荣誉变化时判断（必填）    |
| SUPERUSERS | int  |   寄    | SUPERUSERS=["123456789"] | nonebot超级管理员，用于判断是否为主人(必填) |
|  bot_name  | str  |   寄    |    bot_name = "AI-Md"    |               bot的昵称(必填)               |
|  chuo_cd   | int  |    0    |       chuo_cd = 10       |             戳一戳的cd（选填）              |

戳一戳的cd默认为0即没有cd

## 感谢：

感谢[@cjladmin](https://github.com/cjladmin)的开源代码，在此基础上修改了bug

以后将持续更新并完善

## 其他插件

[使用API的chatGPTQQ聊天机器人](https://github.com/Reversedeer/nonebot_plugin_chatGPT_openai)

[舔狗日记](https://github.com/Reversedeer/nonebot_plugin_dog)
