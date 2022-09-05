# 本研踏勘 #笔记

## 一、本研基础流程

> [参照模块](../../project/本研/README/README.md)

1. 数据获取
   1. 手段：购买数据为基础、爬虫爬取为补充
2. [实地踏勘](#二踏勘需求)
   1. 目的
      1. 筛选变量：便于数据分析展开
      2. 了解当地变量背景：便于数据分析解释
3. [数据分析](#三stata实现)
   1. **手段**
      1. 总体性区位指数（Moran/Geary/散点图/LISA等）
      2. 结构性变量回归（stata双差分模型回归）
4. 报告撰写
   1. 基本脉络

      ```mermaid
      graph LR
      引言-.->文献综述==>理论思路-.->实践操作==>结果分析拓展-.->结论与建议
      ```

   2. 参考文献
      1. [地铁开通对城市房价的影响——基于厦门](https://kns.cnki.net/KXReader/Detail?invoice=skOndDLpdMFT33zar2NQWcmk30zzNKhpnv84sAfO28T9L%2BT4oETgaE%2B0hVZKZWa39X2gOHkVMtTfuiSLf8fgFUqowxYJ4nc5EeUT4Ucydo06wB%2BY7p00K674FnazuskTdHDSU4fN7YhAdghg6%2BADumXkB5q376kfqcJDRWoH%2FOE%3D&DBCODE=CJFD&FileName=JMDZ202203007&TABLEName=cjfdlast2022&nonce=8C3D58E958424F089255720157906EF8&uid=&TIMESTAMP=1658276419923)

## 二、踏勘内容

|目的|解释|
|:--:|--|
|**筛选变量**|在分析前，通过**当地背景环境、调研情况**筛选 ***相关性强的变量*** 引入分析回归|
|**了解当地变量背景**|在分析中/后，通过**当地背景环境**以 ***解释正确的变量反应方向和幅度*** / ***发现错误的变量问题***|

## 三、数据分析

### 1. 模型建立

1. 模型：$lnHpriceit=α0+φSubwayit×Afterit+γControlit+δj+λt+εit$
2. 变量：![Control变量](https://raw.githubusercontent.com/dsw676676/picture/main/image/%E7%9B%B8%E5%85%B3%E5%8F%98%E9%87%8F.png)

### 2. 数据使用

1. 通过[模型变量](#1-模型建立)对arcgis数据分组
2. arcgis数据计算，得到对应变量

### 3. 数据分析

1. 现有工具
   1. 系统命令：windows/linux
   2. 分析工具：[stata](../../基础代码学习笔记/stata.md)/SPSS
   3. 代码工具：python/markdown
   4. 发布工具：git/docsify/hexo
2. 分析方法：stata双差分尝试
   1. 时间/空间固定效应：**单级移动/多级比较**
