# TMS台服冒险岛网页登录器
> 因为台服冒险岛网页登录需要切换繁体环境和登录需要获取随机密码，所以结合其他人代码写了一个精简的网页登录器（总共19行代码）
>> **本教程不直接提供程序，请自行参考下面教程编译exe，防止被注入病毒**
>>
>> 教程比较废话，旨在小白也能编译成功，大佬勿喷
> 
> 工具的下载地址都是给的github地址，有能力的玩家可以自行查看其代码
> 
> 不推荐下载来源不明的工具，以免下载到恶意修改的版本

## 环境初始化
### Python安装（已配置略过即可）
> 为了后续编译源代码
- 参考（第一节）：https://zhuanlan.zhihu.com/p/111168324
### 配置Locale Emulator(已配置略过即可)
#### 下载
> Locale emulator是模拟语言环境的软件，本文使用此软件是为了**生成模拟台湾繁体环境的快捷方式**
>
>> 下载地址：https://github.com/xupefei/Locale-Emulator/releases
> 
> 目前最新v2.5.0.1，下载assets里面的Locale.Emulator.2.5.0.1.zip即可

#### 配置
- 参考：https://ngabbs.com/read.php?tid=21293211&rand=334
- 参考文档执行到1.2步骤即可，生成桌面快捷方式（一般电脑会隐藏后缀名）**MapleStory.lnk**
- 最后一步【替换启动程序】步骤需要这个快捷方式

## 替换启动程序
### 编译源码（必须步骤，取得MapleStory.exe）
> 步骤1和步骤2任选其一即可；步骤3可以直接在源码文件目录的窗口输入cmd，即可打开cmd并自动跳转到此目录
- 1.下载：点击本项目的(绿色按钮)Code -> Download ZIP -> 解压缩
- 2.复制：直接复制本项目的MapleStory.py内容到本地文件
- 3.打开MapleStory.py所在文件夹，在左上角地址栏输入cmd并回车，弹出cmd窗口，依次执行以下命令
- 4.执行命令后，会在目录下会生成一个dist和build文件夹，其中dist里面会有一个**MapleStory.exe**
- 5.最后一步【替换启动程序】步骤需要这个exe文件
```bash
# 设置pip镜像源为阿里云和安装必须的py依赖包
# 复制下面5行代码，在cmd窗口依次执行。如果遇到报错，则是第一步环境初始化没有成功
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
pip install psutil
pip install pyinstaller

# 编译py源码为exe，生成地址在同目录的dist下，名称为MapleStory.exe，根据py文件同名生成，如果名称不对则自行重命名即可
pyinstaller.exe -F -w MapleStory.py
```
---
### 替换启动程序（关键）
- 1.把枫之谷游戏根目录的MapleStory.exe重命名为MapleStory2.exe
- 2.把编译步骤编译好的MapleStory.exe和使用Locale Emulator生成的快捷方式MapleStory.lnk放到同一个目录（任意位置）下
- 3.启动游戏：使用IE浏览器访问hk.beanfun.com或台号官网，登录账号后，依次点击綫上游戲 --> 楓之谷 --> 啓動 --> 然後游戲賬號 --> 開始遊戲
- 4.因为第1步修改名称的原因，导致找不到相应的启动程序，网页会提示你"無法正確偵測遊戲安裝狀態"。并且出现两个按钮，选择左边的已安装，再选择第2步的目录的MapleStory.exe启动
- 5.把第1步的MapleStory2.exe改回MapleStory.exe
- 6.重新执行第3步启动游戏即可
- 7.等待几秒，弹出开始游戏界面，点击开始即可
- 8.以后启动游戏直接执行**第3步**即可

