## 后端安装运行说明

### 语言环境

```python
python
django
```

### IDE

PyCharm     [下载地址](https://www.jetbrains.com/pycharm/?fromMenu)

### Interpreter&&Packages

Interpreter需要本地的python.exe

![](./img/1.png)

### DataBase

**MySQL**

- 本地需要先新建数据库django

- setting.py中DATABASES修改为本地的用户名与密码

- 执行以下命令
```python
python manage.py makemigrations
python manage.py migrate
```

### 运行中版本问题

- decode相关错误，且本机python版本为3+，则找到对应报错代码，将decode改为encode

- pymysqlclient版本报错没有高于1.3.3，找到对应报错代码，将提示报错的if语句注释

### 外网访问本机运行的网页

[ngrok下载](https://ngrok.com/download)

- 解压后运行程序
- 在程序内输入下列命令
    ```python
    ngrok authtoken 5cPJx41mf38znaQ96ofth_2ofQxozFbdZ5pNRv3D5PJ
    ngrok http 80  //80为端口号，可改
    ```
- setting.py中ALLOWED_HOSTS加入ngrok的Forwarding域名
- 本机运行，外网通过Forwarding域名访问
    ![](./img/2.png)