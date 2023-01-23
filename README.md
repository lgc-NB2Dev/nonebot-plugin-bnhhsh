<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-bnhhsh

_✨ 「不能好好说话！」 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/lgc2333/nonebot-plugin-bnhhsh.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-bnhhsh">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-bnhhsh.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<a href="https://pypi.python.org/pypi/nonebot-plugin-bnhhsh">
    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-bnhhsh" alt="pypi download">
</a>

</div>

## 📖 介绍

今晚看到莉沫酱的一个奇奇怪怪的项目[bnhhsh](https://github.com/RimoChan/bnhhsh)，所以心血来潮做了个插件玩！

这个项目也有受到莉沫酱TG群里的黄巍Bot启发

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-bnhhsh

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-bnhhsh
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-bnhhsh
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-bnhhsh
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-bnhhsh
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_bnhhsh')

</details>

<details>
<summary>从 github 安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库

    git clone https://github.com/lgc2333/nonebot-plugin-bnhhsh.git --recursive

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('src.plugins.nonebot_plugin_bnhhsh')

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|       配置项        | 必填 | 默认值  |                      说明                      |
|:----------------:|:----:|:----:|:--------------------------------------------:|
| `BNHHSH_UNV_MSE` | 否 | `0.2` | `unvcode`的字符串不同阈值<br>（如`0.2`则会匹配80%相似度以上的字符） |

## 🎉 使用

插件使用正则匹配所有纯字母消息，并以空白符为分隔符分割每个单词，然后自动将转换结果发送出来～  
具体安装插件自己体验一下就知道了哦～mua～

<!--
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 指令1 | 主人 | 否 | 私聊 |配置说明 |
| 指令2 | 群员 | 是 | 群聊 |配置说明 |
### 效果图
如果有效果图的话
-->

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [RimoChan](https://github.com/RimoChan/)

- 依赖包的作者！经常做些有脑洞的有趣的东西～
- p.s. ~~如果你喜欢TA的作品，请多多给TA发萝莉色图(~~
- p.s.. ~~也给我发点awwa((~~

## 💰 赞助

感谢大家的赞助！你们的赞助将是我继续创作的动力！

- [爱发电](https://afdian.net/@lgc2333)
- <details>
    <summary>赞助二维码（点击展开）</summary>

  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)

  </details>

## 📝 更新日志

### 0.1.2

- 加入[unvcode](https://github.com/RimoChan/unvcode)反和谐，让Bot再色色也不会让勾八tx自动检测～

### 0.1.1

- 修复正则错误匹配**含有**英文的消息而不是**纯**英文消息
