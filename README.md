# TMS台服冒险岛网页登录器
> 自用网页登录器（总共19行代码）
>> 原理是获取网页登录的授权参数，添加到启动程序
>> 简单说就是桃僵李代
> 不推荐下载来源不明的工具，以免下载到恶意修改的版本

## 环境要求
- Python3(编译本项目源码)
- Locale_Remulator配置(生成模拟台湾繁体环境快捷方式)[https://github.com/InWILL/Locale_Remulator/releases]
  - LR配置参考：https://tieba.baidu.com/p/7934812236

## 源码编译（取得MapleStory.exe）
```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
pip install psutil
pip install pyinstaller

# 编译py源码为exe，生成地址在同目录的dist下，名称为MapleStory.exe，根据py文件同名生成，如果名称不对则自行重命名即可
pyinstaller.exe -F -w MapleStory.py
```

## 替换启动程序
- 0.开启加速器
- 1.把枫之谷游戏根目录的MapleStory.exe重命名为MapleStory2.exe
- 2.把编译步骤编译好的MapleStory.exe和使用Locale Emulator生成的快捷方式MapleStory.lnk放到同一个目录（任意位置）下
- 3.启动游戏：使用浏览器访问hk.beanfun.com(港号)或台号官网(台号)，登录账号后，依次点击綫上游戲 --> 楓之谷 --> 啓動 --> 然後游戲賬號 --> 開始遊戲
- 4.因第1步修改名称，导致 開始遊戲 后找不到相应的启动程序，网页会提示"無法正確偵測遊戲安裝狀態"。并且出现两个按钮，选择左边的已安装，再选择第2步的目录的MapleStory.exe启动
- 5.把第1步的MapleStory2.exe改回MapleStory.exe
- 6.重新执行第3步启动游戏即可
- 7.等待几秒，弹出开始游戏界面，点击开始即可
- 8.以后启动游戏直接执行**第3步**即可
