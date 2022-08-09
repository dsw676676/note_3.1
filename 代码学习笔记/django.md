# [Django学习笔记](https://www.runoob.com/django/django-first-app.html) #笔记

- [[Django学习笔记] #笔记](#django学习笔记-笔记)
  - [一、简介](#一简介)
    - [1. 模型](#1-模型)
    - [2. 安装](#2-安装)
    - [1. 创建项目](#1-创建项目)
  - [二、内容](#二内容)

## 一、简介

### 1. 模型
| 模型 | 含义 |控制方法|
| :-- | --- | --- |
|MVC模型|Model View Controller| ![20220806151243](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220806151243.png) |
|MTV模型|Model Template View| ![20220806151443](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220806151443.png) |
> 核心区别：
> 1. MTV模型增设URL分发器，能够将URL的页面请求分发给不同View处理
> 2. MTV模型具有Template，负责将页面(html)展示给用户

### 2. 安装
1. 下载： Django 压缩包，解压并和 Python安装目录放在同一个根目录，进入 Django 目录，执行 python setup.py install，然后开始安装，Django 将要被安装到 Python 的 Lib下site-packages。
2. 配置：环境变量添加
3. 检查：使用终端代码
    ```python
    import django
    django.get_version()
    ```
> 需要进一步搜索vscode的django配置方法 #未完成

### 1. 创建项目
1. 使用工具：python, Django管理工具`Django-admin`
   1. 可用命令：check
    compilemessages, createcachetable, dbshell, diffsettings, dumpdata, flush, inspectdb, loaddata, makemessages, makemigrations, migrate, runserver, sendtestemail, shell, showmigrations, sqlflush, sqlmigrate, sqlsequencereset, squashmigrations, startapp, startproject, test, testserver
2. 流程
   1. 创建项目
       ```python
       django-admin startproject HelloWorld
       ```
   2. 查看目录结构
       ```python
       cd HelloWorld
       tree
       ```

## 二、内容