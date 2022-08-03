# 尝试
- [尝试](#尝试)
  - [一、markdown基本语法](#一markdown基本语法)
    - [1. 内容](#1-内容)
    - [2. 条块](#2-条块)
    - [3. 快捷键](#3-快捷键)
  - [二、MPE拓展语法(谨慎使用)](#二mpe拓展语法谨慎使用)
    - [1. 幻灯片](#1-幻灯片)
    - [2. 目录](#2-目录)
    - [3. 绘图](#3-绘图)
    - [4. 可执行代码块](#4-可执行代码块)
  - [三、主要使用分工](#三主要使用分工)
    - [1. markdown all in one](#1-markdown-all-in-one)
    - [~~2. markdown preview enhanced~~](#2-markdown-preview-enhanced)
    - [3. markdown paste](#3-markdown-paste)
  
## 一、markdown基本语法
### 1. 内容
   1. #### 标题
   2. **加粗**
   3. *倾斜*
   4. ~~删除~~
   5. `代码`
   6. 数学：$\frac{\beta}{\alpha}=\frac{\sqrt{x}}{\sqrt{x+y}}$
   7. [链接](test.md)
   8. ![图片]()
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
### 3. 快捷键
   Key|Command
   :--|--:
   Ctrl + B|Toggle bold
   Ctrl + I|Toggle italic
   Alt + S|Toggle strikethrough
   **Ctrl + Shift + ]**|**Toggle heading (uplevel)**
   **Ctrl + Shift +\[**| **Toggle heading (downlevel)**
   **Ctrl + M**|**Toggle math environment**
   Alt + C|Check / Uncheck task list item
   Ctrl + Shift + V|Toggle preview
   Ctrl + K V|Toggle preview to side


## 二、MPE拓展语法(谨慎使用)

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

## 三、主要使用分工

### 1. markdown all in one
1. 自动补全、换行
2. 提供目录：`Ctrl+Alt+P`
3. 书写数学公式：`Ctrl+M`
### ~~2. markdown preview enhanced~~
1. ~~制作幻灯片、绘图~~
2. ~~导出pandoc~~
3. ~~调换格式~~
### 3. markdown paste
1. 粘贴图片
