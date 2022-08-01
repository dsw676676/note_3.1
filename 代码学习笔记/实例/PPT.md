# MPE-PPT基础介绍
---
[toc]



## 一、Front-Matter基础语法
---
### 1. 分页方法
`<!-- slide -->`
### 2. Front-Matter内容
|名称|含义|选项|
|:--|--|--:|
|theme|主题|beige/black/blood/league/moon/night /serif/simple/sky/solarized/white/none|
|width/height/margin/center|位置宽高|`num`, true/false|
|progress/slideNumber/overview/controls|显示控件|true/false|
|mouseWheel/autoSlide|控制|true/false, `num`|
|transition/transitionSpeed|切换|none/fade/slide/convex/concave/zoom, default/fast/slow|
|**parallaxBackground**Image /.Size/.Horizontal/.Vertical|背景图片|`"situ"`/`num`/null|


## 二、实例示范
<!-- 使用方法：减少缩进+迁移front-matter -->
    ---
    presentation:
        theme: blood.css
        mouseWheel: true
        parallaxBackgroundImage: 'https://res.9game.cn/community/forum/202110/08/150849gyt7ypeee2jmtyj1.jpg'
        parallaxBackgroundSize: "1600px 900px"
        transition: 'zoom'
    ---
    <!-- slide -->
    ## 第一章
    ---
    <!-- slide -->
    ### 第一节
    1. 内容1
    2. 内容2
    <!-- slide -->
    ### 第二节
    1. 内容1
    2. 内容2
    <!-- slide -->
    ### 第三节
    1. 内容1
    2. 内容2
    3. 内容3