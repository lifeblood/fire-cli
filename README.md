
# FIRECLI
基于Google Python Fire库，设计的一套命令行模式下具有MVC理念的微型框架


FIRECLI把那些烦人的定位参数，可选参数等等全部进行了封装，你只要专注业务逻辑部分。

不需要花很大的力气在熟悉argparse等库存的用法上面。节省的大量的精力和时间。


## 目录结构


````
.
├── controllers #存放业务脚本
│   ├── __init__.py
│   ├── template.py
│   └── test.py
├── main.py # 入口程序
├── README.md
├── requirements.txt 
└── ulitilies  # 存放自定义实用工具类
    ├── __init__.py
    └── telegrambot.py
    
````


### 程序运行

````
python main.py test hello

test --> controllers/test.py

````
