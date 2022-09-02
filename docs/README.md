# 本研主体介绍

- [本研主体介绍 #README](#本研主体介绍-readme)
  - [一、推进脉络](#一推进脉络)
    - [1. 总体步骤](#1-总体步骤)
    - [2. python数据爬取](#2-python数据爬取)
    - [3. “变量-距离-房价”模型构建](#3-变量-距离-房价模型构建)
    - [4. stata分析](#4-stata分析)
  - [二、pack内容](#二pack内容)
  - [三、相关语法学习](#三相关语法学习)
    - [1. git同步](#1-git同步)
    - [2. python语法进阶](#2-python语法进阶)

## 一、推进脉络

### 1. 总体步骤

|步骤| 当今成果| 未来问题 |
| :-----: | :----- | :----- |
| [python变量数据爬取](#2-python数据爬取) | [基本框架](..pack/../../pack/_4output/file_work.py)已完成，以此为基础修改表头，即可爬取不同网站数据| 网站数据整合问题(not fit?) |
| [**“变量-距离-房价” 模型构建**](#3-变量-距离-房价模型构建) | [参考文献进行](https://kns.cnki.net/KXReader/Detail?invoice=skOndDLpdMFT33zar2NQWcmk30zzNKhpnv84sAfO28T9L%2BT4oETgaE%2B0hVZKZWa39X2gOHkVMtTfuiSLf8fgFUqowxYJ4nc5EeUT4Ucydo06wB%2BY7p00K674FnazuskTdHDSU4fN7YhAdghg6%2BADumXkB5q376kfqcJDRWoH%2FOE%3D&DBCODE=CJFD&FileName=JMDZ202203007&TABLEName=cjfdlast2022&nonce=8C3D58E958424F089255720157906EF8&uid=&TIMESTAMP=1658276419923) | |
| [stata分析](#4-stata分析) | 基本框架已完成| 分析方法是否全面/规范？ |

### 2. python数据爬取

1. 模型问题
   1. 位置外的其他因素会相当大程度的影响房价，如楼层、装修配置、户型、微型基础设施分布。
   2. 在此基础上作图未能得到好结果（内生性过大）

      ![20220806143205](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220806143205.png)
2. 数据问题
   1. 需要引入更多数据——
      |          | 横轴      | 纵轴         |
      | -------- | --------- | ------------ |
      | 当下     | 地点      | 时间         |
      | **目标** | 地点+时间 | 其他控制变量 |
3. 平台问题
   1. [安居客平台](https://www.anjuke.com)多个文献使用数据源。本身在2020年后不再开放历史房价数据查询和api端口。
   2. [贝壳找房平台](https://dg.ke.com/xiaoqu/c5417952092991112/?sug=G1%E8%9C%82%E6%B1%87)反爬虫能力弱。但信息量与变量数较少，难以支撑进一步分析。
   3. [链家网平台](https://dg.lianjia.com/chengjiao/)能够搜索到历史成交小区数据，通过爬取信息可能能够实现。当前想通过修改 `贝壳找房平台`的相关代码，进行爬取。但相关历史成交数据只有2020年后数据。
   4. [58同城](https://dg.58.com/xiaoqu/)能够对相关内容进行较好的补足

   ```mermaid
   sequenceDiagram
      title file_work
      note over lst: 核心程序（session表头确立/search/query/IP池构建）
      note over json: 中继暂存
      note over excel: 可视化处理
      excel-->>lst: fetch
         lst->>+lst: search_all: xpinyin进行拼音索引
      lst-->>json: push
         lst->>lst: query_all: request+session请求/soup淘洗
      lst-->>json: push
      lst-->>excel: sync
   ```

4. 探索过程
   1. 正向搜索：寻找更全面的数据源
   2. 反向补全：将现有数据的更多信息补全(探索核心与pack实现重点)
   3. 爬虫优化
      1. 使用api请求数据方法(所需信息)
      2. 通过matplotlib简要可视化分布情况

> 进一步发展：补全相关内容数据 #未完成

### 3. “变量-距离-房价”模型构建

> 注释：需要相关内容补足

### 4. stata分析

> 注释：固定效应模型+区位分布指数

## 二、pack内容

1. [file_treat](../pack/_1file_treat/__init__.py)：具有文件转换处理的初步功能，能够实现[json/excel/list的互相转换](../pkack/_1file_treat/excel_json_lst.py)
2. [situation](../pack/_2situ/__init__.py)：具有爬虫的初步功能，能够实现[地理坐标爬取](../pack/_2bug/situ.py)
3. [information](../pack/_3info/__init__.py)：具有爬虫的初步功能，能够实现[表头设置](../pack/_3info/_1info_session.py)、[关键字搜索](../pack/_3info/_2info_search.py)、[属性爬取](../pack/_3info/_3info_query.py)
4. **[output](../pack/_4output/file_work.py)：将爬虫程序相整合，能够完整爬取相关程序**
5. [data](../pack/data/东莞名称.xlsx)：数据输出库，其中表格便于可视化
6. ~~analyse：进一步分析程序（尚未进行）~~

   ```mermaid
   graph TD
      A(修改代码)
      B{数据比较}
      C(进一步分析)
      D(重新寻找网站)
      A==>|爬取成功|B
      A-->|爬取失败|D
      B==>|数据全面|C
      B-->|数据不全面|D
      D-.->|重试|A
   ```

## 三、相关语法学习

### 1. git同步

1. 初始库

   ```mermaid
   graph LR
      github创建库 --> 克隆库 --> 初次更新上传
   ```

2. 更新库

   ```mermaid
   graph LR
      暂存 --> 提交 --> 推送
   ```

3. [创建ssh](https://cloud.tencent.com/developer/article/1444372#:~:text=%E5%9C%A8github%E7%BD%91%E7%AB%99%E4%B8%8A%E6%89%BE%E5%88%B0ssh%E8%AE%BF%E9%97%AE%E7%9A%84url%EF%BC%9A%20%E4%BD%BF%E7%94%A8%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%88%87%E6%8D%A2%E6%88%90ssh%E6%96%B9%E5%BC%8F%E8%AE%BF%E9%97%AE%EF%BC%9A%20git%20remote,set-url%20origin%20git%40github.com%20%3Ai042416%2FKnowlegeRepository.git)

   ```ssh码
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCuRVfRUm49WS6MjAwMKKLIvBIgWzcOcXN1JarzCZ/ktNTUE4jaUMew4soocA9NgfVBWgDZVWaeoHTbsLYNtWBbtRrlThmuspYr30zSeeeKzxWDHFEO6nbTQracTxU/8bNJcd2mW+4IYBCxrJLxlQ/iINV+pv2v8ikpgZkgzQu7dHb9mFgTWj9FrXAvdp/ebno1rCXw5K64w2JinJ99KqD+rgbsmH9Ep6RlzUczQBZrp2O4C8dDLG+uOWo2yVntivm39JDrnKIIgul9AciYva4AXNeDuR8Hr/w7c1ji7rylVlnwSnndbeK9orRkJlC8zsI2CDd+GQYk7vNGo/G4e/NcJLWdXMYLRBWde2PuuG9y0ulX+1zceOqdjJI1K/5lg5WB4WeCr3qjdNx1dtX3dezdRre79LxPfE34OE9MGmVC+AmnNciPqED3HdiVixadz8SoHf0ZicmbC/rmjuKEexHwHkJw9KcKK02qAO0u+kvr8ViG4c3qbg13lRCdIUcVt3zN8BkGbHBmOXey4qZG5o2BFGyfiEGMq9myhmKnCQ6baPyTGD19nzi6XPhypehhWIY2pdwqRfUMaZrizMrF1X8IloMjep6UOXFme/XI+k+JjRBumwuoBEqntcydt7wm2x2H4wqpqzhZdvQbbROPe9uf40b/N5cJFgygBxVvDrXBEQ== dsw676676@gmail.com
   ```

4. [创建token](https://blog.csdn.net/qq_35621494/article/details/106432399)

   ```token
   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
   ```

### 2. python语法进阶

1. 模块引用：from import
   | 程序     | 方法              |
   | -------- | ----------------- |
   | 同级目录 | *.path*           |
   | 不同目录 | sys.path.append() |
2. 打包格式：tap式框架+引用关系+注释文档
