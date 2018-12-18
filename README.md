# mz_api
使用face_recognition让你实现在线试妆~

## DEMO
http://ai.clf.red
(注：本项目没有前端页面，请自行构建)

## 环境
Python 3

## 安装库

```
pip install face_recognition
pip install django
```

## 使用

#### 运行
在mz_web目录下：
```
python manage.py runserver
```
#### 请求
请求方式：post
请求地址：http://localhost:8000/mz_api
请求参数：
```
r:口红色号R值 
g:口红色号G值
b:口红色号B值
key:随机字符串
img:人脸正面照
```
