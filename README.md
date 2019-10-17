
# FIRECLI [![Build Status](https://travis-ci.org/lifeblood/firecli.svg?branch=master)](https://travis-ci.org/lifeblood/firecli)


基于Google Python Fire库，设计的一套Python命令行模式下具有MVC理念的微型框架

FIRECLI把那些烦人的定位参数，可选参数等等全部进行了封装，你只要专注业务逻辑部分。

不需要花大力气去熟悉argparse, click等库的用法, 提升运维日常脚本开发效率。


## 目录结构


````
.
├── bootstrap  #业务引导类
│   ├── app.py
│   └── __init__.py
├── config  #配置文件
│   └── config.ini
├── controllers  # 业务脚本存放目录，并自动注入到入口程序
│   ├── __init__.py
│   ├── template.py  # 业务类模板
│   └── test.py    # 具体业务类
├── main.py   统一入口程序
├── README.md
├── requirements.txt
└── ulitilies   # 存放自定义实用工具类
    ├── fireconfig.py
    ├── __init__.py
    └── telegrambot.py # 纸飞机机器人实用类
    
    
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
