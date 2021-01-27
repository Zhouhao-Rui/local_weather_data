# --自动化爬虫天气网站数据并做成API接口

## 1. scrapy 爬取数据

- 使用item.py定义网站上的数据类型，然后使用spider进行网络请求爬虫
- settings里面Robots = False
- settings里面定义mongodb的相应内容
- 安装pymongo包
- 在pipeline里面将对应的item存放到对应的collection中
- 写一个入口文件，默认执行每天执行一次scrapy crawl spider命令

## 2. centos安装python

​	centos7默认的安装版本是2.7，我们需要使用python3, 所以需要重新安装

<p style="color: #f40"><b>注意：在安装python3之前需要安装一系列的依赖包</b></p>

- ```shell
  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel qlite-devel readline-devel tk-devel libffi-devel
  ```

- 然后使用wget得到相应的python版本

  

```shell
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar -zxvf Python-3.7.4.tgz
cd Python-3.7.4 && ./configure prefix=/usr/local/python3
make && make install
```

- 创建软连接

```shell
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

## 3. centos安装mongo

- 依照官网的操作，使用yum安装
- 使用iptables开启远程数据库连接

## 4.  安装scrapy

- 安装twisted依赖包
- 安装scrapy
- 创建项目，将相应的代码移植
- 启动项目

## 5. 安装nodeJs

- 使用yum install nodejs
- 当前版本过旧，使用npm install n -g
- 然后 执行n lts， node版本升级到了12
- exit当前连接
- 重新进入已经成功更新了node和npm

## 6. node项目做API接口

- 使用express框架创建项目
- 使用mongoose创建schema，定义model
- 使用get请求从远程mongodb得到相应的数据，写在两个不同的路由上

## 7. 将node项目移植到远程服务器上

- 使用git，push代码到repository中
- 服务器拉取git代码，使用npm i安装依赖库
- 全局安装PM2，后台启动服务

## 8. 使用Nginx对node项目反向代理

- 使用proxy_pass进行反向代理

```nginx
server {
    listen server_port;
    listen [::]:server_port;
    server_name your_domain;
    access_log /var/log/nginx/domain1.access.log;
    location / {
        proxy_pass    http://127.0.0.1:your_port/;
    }
}
```

## 9. 运行项目，查看是否成功
