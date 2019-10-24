
# FIRECLI [![Build Status](https://travis-ci.org/lifeblood/fire-cli.svg?branch=master)](https://travis-ci.org/lifeblood/firecli)


基于Google Python Fire库，设计的一套Python命令行模式下具有MVC理念的微型框架

FIRECLI把那些烦人的定位参数，可选参数等等全部进行了封装，你只要专注业务逻辑部分。

不需要花大力气去熟悉argparse, click等库的用法, 提升运维日常脚本开发效率。

## 主要功能

config key value配置功能，配置文件：config/config.ini

类似 laravel/lumen的访问路由配置协议，配置文件：routes/route.py

## 目录结构


````
    
├── bootstrap # helpers业务引导类
│   ├── app.py
│   └── __init__.py
├── config  #文件配置目录
│   └── config.ini
├── controllers  # 业务脚本存放目录，并自动注入到入口程序
│   ├── __init__.py
│   ├── template.py
│   └── test.py
├── helpers  内置助手类
│   ├── fireconfig.py
│   ├── __init__.py
│   └── utils.py
├── main.py
├── models  # 自定义业务类
│   ├── __init__.py
│   └── telegrambot.py
├── README.md
├── requirements.txt
└── routes
    ├── __init__.py
    └── route.py   # 控制层路由配置文件
    
````

### 生成 requirements.txt 
````
pip freeze > requirements.txt
````

### 程序运行

````
python main.py test hello

test --> controllers/test.py

hello --> controllers/test.py method

````
