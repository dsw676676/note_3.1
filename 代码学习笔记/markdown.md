# Markdown总览 #笔记

- [Markdown总览 #笔记](#markdown总览-笔记)
  - [一、markdown基本语法](#一markdown基本语法)
    - [1. 内容](#1-内容)
    - [2. 条块](#2-条块)
    - [3. 快捷键](#3-快捷键)
  - [二、插件分工](#二插件分工)
    - [1. markdown all in one](#1-markdown-all-in-one)
    - [2. picgo](#2-picgo)
    - [~~3. markdown preview enhanced~~](#3-markdown-preview-enhanced)
  - [三、Markdown-Math](#三markdown-math)
    - [1.总结](#1总结)
    - [2.罗列](#2罗列)
  
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
      print("code trunk")```
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

## 二、插件分工

### 1. markdown all in one
1. 自动补全、换行
2. 提供目录：`Ctrl+Alt+P`
3. 书写[数学公式](#四markdown-math) ：`Ctrl+M`
### 2. picgo
1. 粘贴图片`Ctrl+Alt+U`
### ~~3. markdown preview enhanced~~
1. 幻灯片
   1. 分页：\<!-- slide_ -->
   2. [样式](实例/PPT.md)：first theme, mouseWheel, transition, progress
2. 目录
   1. 简单：[toc]
   2. 复杂：Ctrl+Shift+P >> Create Toc
3. 绘图
   1. [mermaid绘图](实例/mermaid.md)
4. 可执行代码块
   ```python{cmd=true}
      print("code trunk")
   ```
5. 导出：pandoc
   
## 三、Markdown-Math

### 1.总结
1. 语法概览
   1. 框架：`$行内$`、`$$行间$$`
   2. 函数：`\func{x}`
   3. 编号：`\tag{}`
2. 常用函数[link]
    | 函数            |              含义 |
    | :-------------- | ----------------: |
    | \begin{} \end{} | 开始结束，如matrx |
    | \sum            |              求和 |
### 2.罗列
$$ \beta = \frac{\sqrt{x}}{\sqrt{y+1}} \tag{2.1} $$

$$ \left|\begin{matrix}
    x & y & z \\
    a & b & c \\
    \end{matrix}\right| \tag{2.2} $$

$$\left|
	\begin{matrix}
		x&y&z\\
		z&x&y
	\end{matrix}
\right|=x+y+z$$
$$ \sum_{i=1}^{\infty}{x+y}=0 \tag{2.3} $$

$$ \sin^2(\theta) + \cos^2(\theta) = 1 \tag{2.4} $$

$$ \sum_{n=1}^{\infty}{k} = 1 \tag{2.5} $$

$$ \int_a^bf(x)\,dx \tag{2.6} $$

$$ \lim_{x\to\infty}\exp(-x) = 0 \tag{2.7} $$