---
presentation:
 theme: league.css
 mouseWheel: true
 parallaxBackgroundImage: 'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg'
---
<!-- slide_ -->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. markdown基本语法](#1-markdown基本语法)
- [2. MPE基本语法](#2-mpe基本语法)
- [3. 基本内容](#3-基本内容)

<!-- /code_chunk_output -->


<!-- slide_ -->
## 1. markdown基本语法
---
<!-- slide_ -->
1. 内容
    1. #### 标题
    2. ==高亮==
    3. **加粗**
    4. *倾斜*
    5. `代码`
    6. ~~删除~~
    7. [链接](test.md)
    8. <img src="" width=50%>
<!-- slide_ -->
2. 条块
    1. |表格|
        |----|
    2. > 注释
    3. 分割线

        ---
    4. 
        ```python{cmd=true} 
        print("code trunk")
        ```

<!-- slide_ -->
## 2. MPE基本语法
---
<!-- slide_ -->
1. 幻灯片
   1. 分页：\<!-- slide_ -->
   2. 样式：theme, mouseWheel, transition, progress
<!-- slide_ -->
1. 目录
   1. 简单：[toc]
   2. 复杂：Ctrl+Shift+P >> Create Toc
2. 样式

## 3. 基本内容
---

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title 为mermaid加入甘特图功能
    section A部分
        完成任务        :done, des1,2019-01-06,2019-01-08
        正进行任务      :active, des2,2019-01-09,3d
        待开始任务      :des3, after des2, 5d
        待开始任务2     :des4, after des3, 5d
    section 紧急任务
        完成任务        :crit,done,2019-01-06,24h
        实现parser     :crit,done,after des1, 2d
        为parser编写test :crit, active, 3d
        待完成任务      :crit,5d
        为rendere编写test: 2d
        将功能加入到mermaid: 1d