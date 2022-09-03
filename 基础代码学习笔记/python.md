# python语法归纳 #笔记

## 一、基础内容

### 1. 数据类型

   |类型|定义|
   |--|--|
   |整形int|`123456`|
   |字符串str|`"HelloWorld"`|
   |布尔型bool|`True`/`False`|
   |元组turple|`(1,2)`|
   |列表list|`[1,2]`|
   |字典dict|`{key: value}`|

### 2. 重要语法

   1. 循环：`for`/`while`/`def递归`+`continue`/`break`
   2. 错误检测：`try: except: else: finally:`
   3. 函数function
      1. 内外变量：`global`
      2. 匿名函数：`lambda定义`+`map应用`
      3. 内置函数

         ![20220806170848](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220806170848.png)
   4. 类class：是对象的实例
      1. 变量类型：全局`global`、局部`local`、类属性`self.sth`
      2. 函数类型：初始函数`self.__init__`、类函数`self.func`

### 3. 编程思维

   |思维|内容|逻辑|
   |--|--|--|
   |面向过程|按照解决问题的步骤撰写代码|基于业务逻辑|
   |函数式 (对[函数](#2-重要语法))|将功能封装到函数中，便于重复使用|基于模块逻辑|
   |面向对象 (对[类](#2-重要语法))||基于设计逻辑|

   object oriented programming

## 二、多线程

1. 实现方法：`函数/类`包装+**模块**执行
   1. _thread方法：函数调用(`start_new_thread()`)
   2. threading方法：类调用(创建`=class`、开启`start()`、结束`join()`)
2. 互斥锁
   1. Thread包的Lock和Rlock对象
      1. 两个对象都有acquire和release方法
      2. **两个方法之间可以插入需要数据同步的步骤**
   2. Queue包加入
      1. **创建workqueue包，作为避免重复处理的对象**
