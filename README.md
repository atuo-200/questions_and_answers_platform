### 基于Flask和MySQL的问答平台demo介绍

此小demo是基于Flask和MySQL搭建起来的问答平台，是在学习过程中按b站：[Python Flask零基础到项目实战系列-项目实战](https://www.bilibili.com/video/BV1ks411P758?p=1) 手敲起来的一个小demo

可把项目代码下载至本地，删除掉migrations目录并进入项目目录中使用以下命令进行数据库迁移

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

但在之前要注意，相关的MySQL连接配置写在config.py中，要根据自身数据库配置进行更改

在进行数据库迁移之后，运行项目代码

+ 可在pycharm中运行项目
+ 也可在命令行中进入项目目录后，运行命令python manage.py runserver

即可在浏览器打开127.0.0.1:5000运行此小demo

可对此问答平台进行注册，相关的用户信息会存至MySQL的user表中，密码字段会加密保存，登录验证时会对密码进行相应的解密再验证

![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B71.PNG)

注册之后可进行登录


![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B72.PNG)

登录之后会跳转至首页，会在右上角会显示登录的用户名，并可对登录的账号进行注销（退出登录）


![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B73.PNG)

在搜索框中搜索相应的字段，只要某问答的标题或内容中存在该字短，该问答就会被搜索出来


![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B77.PNG)

点击首页中的问答链接会跳转到相关的问答详情界面中，并可对询问的问题添加回答

![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B76.PNG)

在发布问答这里可以添加自己的问答（这里做了登录限制，如果是未登录状态发布问答，会跳转至登录界面）
![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B74.PNG)

添加的问答会显示到首页

![image](https://github.com/atuo-200/flask_questions-and-answers_demo/blob/master/demo-img/%E6%8D%95%E8%8E%B75.PNG)
