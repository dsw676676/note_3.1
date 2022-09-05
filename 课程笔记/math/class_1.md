# 第一章 函数与极限 #math_note

## 一、实数

1. 数域类型
   1. $R=\{-\infty,\infty\}$
   2. $N$：自然数
   3. $Z$：整数
   4. $Q$：有理数即分数，能够表示为两个正整数之比
2. 实数集$R$的特征
   1. **数域特征**：对加减乘除封闭，可以以此证明有理数
   2. 运算律：对乘法/加法符合交换/结合/分配律
   3. 有序性：任意两个不同的数都有大小关系
   4. 完备性：实数充满了整个数轴(连续性)
3. 数轴与区间
   1. $[x,y)$：区间
   2. $\exist$：存在
   3. $\exist!$：存在且唯一
   4. $\forall$：对所有
4. 绝对值不等式
   1. 定义

		![20220905201402](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220905201402.png)

		![20220905201441](https://raw.githubusercontent.com/dsw676676/picture/main/image/20220905201441.png)

## 二、函数

### 1. 基础定义

   1. 定义域domain：X
   2. 陪域condomain：Y
   3. 值域range：f(x)
		$$\begin{matrix} f(x)&=&\{f(x):x \in X\} \\ f(x)&\subset&Y \end{matrix}$$

   4. 映射关系：对每一个X定义域中的x，有且仅有一个Y值域中的y与之对应。
		$$f: \begin{cases}X & \to & Y \\ x & \to & y \end{cases}$$

### 2. 初等函数类型

   1. 常值函数
   2. 幂函数
   3. 指数函数
   4. 三角函数

### 3. 反函数映射关系

   1. 映射：$f:E\to F$
   2. 满射(onto)：陪域=值域
   3. 单射(one-to-one)
   4. 双射(bijective)：满射且单射

### 4. 复合函数

$$Def\
\begin{cases}
	f:X \to Y, \\ g:Y^* \to Z
\end{cases}\\
We\ have\ (g \circ f)(x) = g(f(x))$$

### 5. 分段函数

1. 特殊函数：$f(x)=\{x\}=x-[x]$
2. Dirichlet函数：$D(x)=\begin{cases}1 & ,x \in Q\\ 0&,x\in R\ but\ Q \end{cases}$
