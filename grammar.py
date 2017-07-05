#encoding="utf-8"

实例ID:i-2ze9sg81jq1isokra7np
实例名称:microsoft-init
公网IP：47.95.2.25
内网IP：172.17.87.34

远程：
安装ssh

mac：
ssh root@47.95.2.25
然后输入密码之类的就可以了。

接下来创建用户：
adduser thomas，然后会输入两次密码，（使用useradd的流程有点不一样，好像不会在/home下创建用户目录
然后打开/etc/sudoers文件，在一行中给新用户sudo权限

http://www.mr-wu.cn/aliyun-ecs-ubuntu/
