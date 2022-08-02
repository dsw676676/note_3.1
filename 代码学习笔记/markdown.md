- [## 一、markdown基本语法](#-一markdown基本语法)
  - [1. 内容](#1-内容)
  - [2. 条块](#2-条块)
- [## 二、MPE拓展语法(谨慎使用)](#-二mpe拓展语法谨慎使用)
  - [1. 幻灯片](#1-幻灯片)
  - [2. 目录](#2-目录)
  - [3. 绘图](#3-绘图)
  - [4. 可执行代码块](#4-可执行代码块)


## 一、markdown基本语法
---
### 1. 内容
   1. #### 标题
   2. ==高亮==
   3. **加粗**
   4. *倾斜*
   5. `代码`
   6. ~~删除~~
   7. [链接](test.md)
   8. <img src="" width=50%>
<!-- slide_ -->
### 2. 条块
   1. |表头|
      |:--|
   2. > 注释
   3. 分割线

        ---
   4. ```python
      print("code trunk")
      ```

## 二、MPE拓展语法(谨慎使用)
---
### 1. 幻灯片
1. 分页：\<!-- slide_ -->
2. [样式](实例/PPT.md)：first theme, mouseWheel, transition, progress
### 2. 目录
   1. 简单：[toc]
   2. 复杂：Ctrl+Shift+P >> Create Toc
### 3. 绘图
   1. [mermaid绘图](实例/mermaid.md)
### 4. 可执行代码块
   1. ```python{cmd=true}
      print("code trunk")
      ```