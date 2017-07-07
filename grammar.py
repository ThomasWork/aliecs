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

修改SSH配置 提升安全性
因为把端口从22改成了2002，所以以后登陆都需要使用2002号端口，ssh -p 2002 thomas@47.95.2.25
然后需要配置访问服务器的规则，配置教程网址：https://help.aliyun.com/document_detail/25475.html?spm=5176.2020520101.121.1.211d5c9aE6FBOp
如果没有配置规则，那么使用-p 2002会提示超时，应该是ali自动把请求给丢弃了

然后在添加了规则允许2002端口访问之后，就可以连接了，因为使用了root账户，输入密码后会提示Permission Denied。换成普通用户就可以登录了。

重启SSH
/etc/init.d/ssh restart，但是禁用了root之后，重启ssh好像root还是可以登录，使用reboot之后root登录就失败了。

在安装了Apache之后，在公网就可以输入IP地址进行访问了。哈哈。


在网站上找到nginx的下载地址。
安装Nginx的网址见：http://www.cnblogs.com/hzh19870110/p/6100674.html
http://nginx.org/download/nginx-1.12.0.tar.gz

进入到目录中：执行./configure
最后有如下输出，最好记下来。

Configuration summary
    + using system PCRE library
    + OpenSSL library is not used
    + using system zlib library
                
nginx path prefix: "/usr/local/nginx"
nginx binary file: "/usr/local/nginx/sbin/nginx"
nginx modules path: "/usr/local/nginx/modules"
nginx configuration prefix: "/usr/local/nginx/conf"
nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
nginx pid file: "/usr/local/nginx/logs/nginx.pid"
nginx error log file: "/usr/local/nginx/logs/error.log"
nginx http access log file: "/usr/local/nginx/logs/access.log"
nginx http client request body temporary files: "client_body_temp"
nginx http proxy temporary files: "proxy_temp"
nginx http fastcgi temporary files: "fastcgi_temp"
nginx http uwsgi temporary files: "uwsgi_temp"
nginx http scgi temporary files: "scgi_temp"

然后
make
sudo make install
sudo /usr/local/nginx/sbin/nginx


因为之前已经安装了Apache服务器，所以它占用了80号端口，需要把它卸载了。卸载网址见：http://blog.csdn.net/dazhi_100/article/details/43121179

安装tomcat前需要安装Java，安装网址为：http://www.linuxidc.com/Linux/2016-11/136958.htm

安装Java缺少命令：sudo apt-get install software-properties-common python-software-properties



安装tomcat：
参考网址：https://jingyan.baidu.com/article/e4d08ffdabb0710fd2f60de9.html
tomcat下载网址为：https://tomcat.apache.org/download-80.cgi
我选的下载包网址：http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.16/bin/apache-tomcat-8.5.16.tar.gz

建站网址：
http://www.banzg.com/archives/category/jianzhan
