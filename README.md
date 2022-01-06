# TMS台服冒险岛网页登陆脚本
> 个人写的直接网页登录的脚本，优势是不需要更换为繁体环境
> 
> 请自行复制源码编译exe，防止被注入病毒
> 
> 工具的下载地址都是给的github地址，有能力的玩家可以自行查看其代码
> 
> 不推荐下载来源不明的工具，以免下载到恶意修改的版本

## 初始化环境(已配置略过即可)
### python安装
- 参考（第一节）：https://zhuanlan.zhihu.com/p/111168324
### 编译源码
- 1.点击本项目的(绿色按钮)Code -> Download ZIP -> 解压缩
- 1.或直接复制本项目的MapleStory.py内容到本地文件
- cmd到源码目录，执行以下代码，在目录下生成一个dist文件夹，dist文件夹里面生成一个**MapleStory.exe**
```bash
# 设置pip镜像源为阿里云
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
# 安装psutil包
pip install psutil
# 安装pyinstaller包
pip install pyinstaller

# 编译py源码为exe
pyinstaller.exe -F -w MapleStory.py
```

## 替换启动程序
### 配置Locale emulator(已配置略过即可)
#### 下载
> Locale emulator是模拟语言环境的软件
>
> 下载地址：https://github.com/xupefei/Locale-Emulator/releases
> 
> 目前最新v2.5.0.1，下载assets里面的Locale.Emulator.2.5.0.1.zip即可

#### 配置
- 参考：https://ngabbs.com/read.php?tid=21293211&rand=334
- 执行到1.2步骤即可，生成桌面图标**MapleStory.lnk**

### 替换启动程序（关键）
- 1.把枫之谷游戏根目录的MapleStory.exe重命名为MapleStory2.exe
- 2.把前面步骤打包好的MapleStory.exe，和使用Locale Emulator生成的快捷方式MapleStory.lnk放到同一个目录（任意位置）下
- 3.启动游戏：使用IE浏览器访问hk.beanfun.com或台号官网，登录账号后，依次点击綫上游戲 --> 楓之谷 --> 啓動 --> 然後游戲賬號 --> 開始遊戲
- 4.因为第1步修改名称的原因，导致找不到相应的启动程序，网页会提示你"無法正確偵測遊戲安裝狀態"。并且出现两个按钮，选择左边的已安装，再选择第2步的目录的MapleStory.exe启动
- 5.把第一步的MapleStory2.exe改回MapleStory.exe
- 6.重新执行第3步启动游戏即可
- 7.等待几秒，弹出开始游戏界面，点击开始即可

