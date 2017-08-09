
#user thomas;
user  nobody nogroup;
worker_processes  1;
#daemon off;#是否以守护进程方式运行
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    client_max_body_size 8M;
    client_body_buffer_size 128K;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
	access_log logs/access.log;
	root /var/www/;
	index index.php index.html index.htm;
        server_name  localhost;	

        #charset koi8-r;

        #access_log  logs/host.access.log  main;
	location /test {
		mytestconf jordan 24;
	}
	location =/ { #匹配根目录
		rewrite ^(.*) http://47.95.2.25/wordpress/ redirect;
	}

        location / { #匹配所有请求
	    try_files $uri $uri/ /index.php?q=$uri&$args;

           # root   wordpress;
           # index  index.html index.htm;
	   # proxy_pass http://localhost:8080;
        }

        error_page  404              /404.html;
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/local/nginx/www;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        location ~ \.php$ {
	    try_files $uri =404;
	   # fastcgi_split_path_info ^(.+\.php)(/.+)$;
	    include fastcgi.conf; #如果不加上这一句会在安装界面显示空白
	  #  fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name; 
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
	    fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
            fastcgi_index  index.php;
            #fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
            include        fastcgi_params;
        }

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}