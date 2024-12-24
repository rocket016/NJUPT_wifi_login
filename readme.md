### 校园网一键登录脚本使用说明

* 适用平台：Windows

* 开发语言：python

之前在IOS看到了一个可以登录的快捷方式，于是萌生出移植到Windows的念头

### 使用说明：

首先，安装依赖

~~~bash
pip install -r requirements.txt
~~~

然后，修改njupt_login.py中最后几行的文件内容：

~~~python
# 改这里的账号密码
username = "usermane"
password = "password"
~~~

修改完成之后，运行

~~~bash
python ./njupt_login.py
~~~

即可登录

### 返回结果状态：

* 登录成功

  ~~~bash
  dr1003({"result":1,"msg":"Portal协议认证成功！"});
  ~~~

* 密码错误：

  ~~~bash
  dr1003({"result":0,"msg":"账号错误(运营商登录请检查输入的账号和绑定的运营商账号是否有误)","ret_code":1});
  ~~~

* 已经登录，无需再次登录

  ~~~bash
  dr1003({"result":0,"msg":"AC999","ret_code":2});
  ~~~



### 双击登录

为了方便使用，可以写一个bat文件，实现双击登录

新建一个bat文件，比如叫做login.bat

python后面填写py文件存放的路径，比如，你存放在D盘下，就写

~~~powershell
python D:\njupt_login.py
pause
~~~

然后把这个bat丢到桌面，就可以双击登录了。



by rocket

2024.12.24

rocket_mail@qq.com