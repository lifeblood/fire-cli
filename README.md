
# FIRE-CLI [![Build Status](https://travis-ci.org/lifeblood/fire-cli.svg?branch=master)](https://travis-ci.org/lifeblood/fire-cli)


基于Google Python Fire库，设计的一套Python命令行模式下具有MVC理念的微型框架

FIRECLI把那些烦人的定位参数，可选参数等等全部进行了封装，你只要专注业务逻辑部分。

不需要花大力气去熟悉argparse, click等库的用法, 提升运维日常脚本开发效率。

## 主要功能


1.config key value配置功能，配置文件：config/config.ini

2.类似 laravel/lumen的访问路由配置协议：routes/route.py

3.内置RPC模块（ RPyC / zeroprc ）


## 目录结构


````
 
├── app
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── sub
│   │   │   ├── __init__.py
│   │   │   └── test.py
│   │   ├── template.py
│   │   └── test.py
│   ├── __init__.py
│   └── models
│       ├── db.py
│       ├── __init__.py
│       └── telegrambot.py
├── bootstrap
│   ├── app.py
│   └── __init__.py
├── config
│   └── config.ini
├── docker-compose.yml
├── Dockerfile
├── firecli
│   ├── core.py
│   ├── database.py
│   ├── __init__.py
│   ├── routing.py
│   └── rpc.py
├── helpers
│   ├── fireconfig.py
│   ├── __init__.py
│   └── utils.py
├── main.py
├── README.md
├── requirements.txt
└── routes
    ├── __init__.py
    └── route.py 
    
    
````

### 生成 requirements.txt 
````
pip freeze > requirements.txt
````

### CLI程序运行

````
python main.py test hello

test --> controllers/test.py

hello --> controllers/test.py method

````

### RPC程序运行(daemon)

````
python main.py -rpc {rpc controller}

````
