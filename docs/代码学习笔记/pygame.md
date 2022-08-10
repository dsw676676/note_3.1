# pygame库学习笔记 #笔记

- [pygame库学习笔记 #笔记](#pygame库学习笔记-笔记)
  - [一、基本介绍](#一基本介绍)
    - [1. 代码基础](#1-代码基础)
    - [2. Surface设置](#2-surface设置)
    - [3. Rect设置](#3-rect设置)
    - [3. Event内容](#3-event内容)
    - [3. Event响应](#3-event响应)
    - [4. 其他绘制](#4-其他绘制)
  - [二、实操心得](#二实操心得)

## 一、基本介绍

### 1. 代码基础
1. 执行流程：`获取/判断/响应/刷新`循环
    
    ![20220807113632](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220807113632.png)
2. 核心概念
   1. Surface绘图平面
   2. Rect矩形区域：通过`get_rect()`方法获得
   3. 对象放置：`blit()`
   4. 界面重绘：`display.flip()`
   5. [窗口主循环](#1-代码基础)
### 2. Surface设置
1. 窗口设置：`pygame.display`
   ```python
   pygame.init()
   screen = pygame.display.set_mode(800,600) # 尺寸
   pygame.display.set_icon(icon) # 图标
   ```
### 3. Rect设置
1. **导入图像**：`pygame.image`
   ```
   sr = pygame.image.load("image.jpg")
   ```
2. 载入物体
   ```
   rectsr = sr.get_rect()
   ```
   1. 能够获得相关一个覆盖图像的矩形Rect对象
   2. Rect对象具有属性
      1. top,bottom,left,right 表示上下左右
      2. width,height 表示宽度、高度
### 3. Event内容
1. 事件捕获：`pygame.event`
   ![20220807141710](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220807141710.png)

2. 处理事件：

    > pygame.event.get()
    > pygame.event.poll()
    > pygame.event.clear()

3. 操作事件队列：

    > pygame.event.set_blocked()
    > pygame.event.get_blocked()
    > pygame.event.set_allowed()

4. 生成事件：

    > pygame.event.post()
    > pygame.event.Event

5. 事件内容：

    表头|内容
    --|--
    event.unicode|按键unicode码，不推荐
    event.key|按键的常量名称![20220807142728](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220807142728.png)
    event.mod|按键修饰符的组合值
### 3. Event响应
|函数|功能|
|---|---|
|`rectsr.move(x,y)`|矩形**偏移**x,y像素|
|`screen.fill(color)`|窗口背景**填充**为color颜色，采用RGB色彩体系|
|`screen.blit(src, dest)`|将一个图像**绘制**在另一个图像上，即将src绘制到dest位置上|
|`pygame.time.Clock()`|创建一个Clock对象，用于**操作时间**|
|`clock.tick(framerate)`|**控制帧速度**，即每秒钟窗口刷新速度|
### 4. 其他绘制
1. 图形绘制：`pygame.draw.?(Surface,color,Rect,width...)`
    
    ![20220807143428](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220807143428.png)
2. 文字绘制：`pygame.freetype.Font`
   1. Rect对象
        ```
        pygame.freetype.Font.render_to(surf, dest, text, fgcolor=None, bgcolor=None, rotation=0, size=0)
        ```
   2. Surface对象
        ```
        pygame.freetype.Font.render(text, fgcolor=None, bgcolor=None,rotation=0, size=0)
        ```

## 二、实操心得