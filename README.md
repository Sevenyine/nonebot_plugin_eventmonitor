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

| config  | type | default |   example    |       usage        |
| :-----: | :--: | :-----: | :----------: | :----------------: |
| chuo_cd | int  |    0    | chuo_cd = 10 | 戳一戳的cd（选填） |

<details>
    <summary><h2>更新日志</h2></summary>

- v0.1.5

  - 优化配置文件 [#issue6](https://github.com/Reversedeer/nonebot_plugin_eventmonitor/issues/6)
  - 删除冗余代码
  - 修复获取superusers数值bug

- v0.1.3
  - 修复配置文件bug
- v0.1.2
  - 增加了戳一戳的文案

  - 修改一些bug
- v0.1.1

  - 好像改了什么..忘了...
- v0.1.0
  - 抛弃原有的配置模式
  - 给戳一戳加了cd（本人觉得功能鸡肋）
  - 修复管理员变动时API报错问题[#issue1](https://github.com/Reversedeer/nonebot_plugin_eventmonitor/issues/1)
- v0.0.6
  - 修复了大量的bug
  </details>

## 关于 ISSUE

以下 ISSUE 会被直接关闭

- 提交 BUG 不使用 Template
- 询问已知问题
- 提问找不到重点
- 重复提问

> 请注意, 开发者并没有义务回复您的问题. 您应该具备基本的提问技巧。  
> 有关如何提问，请阅读[《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)

## 感谢：

感谢[@cjladmin](https://github.com/cjladmin)的开源代码，在此基础上修改了bug

以后将持续更新并完善

## 其他插件

[使用API的chatGPTQQ聊天机器人](https://github.com/Reversedeer/nonebot_plugin_chatGPT_openai)

[舔狗日记](https://github.com/Reversedeer/nonebot_plugin_dog)
