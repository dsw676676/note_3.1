## 2022/8/2 Tuesday
### 已完成
1. 找寻到了58同城爬虫内容
    | 时期 |               想法                |             爬虫内容 |
    | :--- | :------------------------------: | ------------------: |
    | 前期 |           从新爬取相关            |      price+situ+info |
    | 中期 |         根据price文档补充         | info`requests/BSoup` |
    | 后期 | 58同城平台锁定+根据拼音绕过反爬虫 |        info`xpinyin` |
### 未完成
1. [x] 未与两位同学回复信息：王欣、accelerator
2. [ ] 爬虫可行性未测试
3. [x] 爬虫后半程未完成


## 2022/8/3 Wednesday
### 已完成
1. 构造基本[proxies爬虫](../../../project/本研/pack2/_3info/_4proxies_get.py)：**api爬取**+清洗+**测试**+输出
2. 重新对58同城网站进行解析
3. 学习Xpath方法
   ```mermaid
   graph LR
      A(begin)-->|import|B{lxml.etree}-->|etree.HTML函数|selector-->|selector.xpath函数|data
   ```
<!-- 1. 基本词性
   | 结构     |       内容        | 一般用词 |
   | :------- | :---------------: | -------: |
   | **主语** |       主动        |        n |
   | **谓语** |     关系/动作     |        v |
   | **宾语** |       被动        |        n |
   | 定语     | 形容**主语/宾语** |    adj的 |
   | 状语     |   形容**谓语**    |    adv得 |
   | 补语     | 补充说明**宾语**  |          |
1. 常用介词充当状语：over
2. 句式
   1. 简单句
      1. **主**+**谓**+**宾**++补+状+定
      2. 主+系+表
   2. 问句
      1. 一般疑问句：be/情态动词+主语+宾语/表语
      2. 特殊疑问句：header+一般疑问句 -->
### 未完成
1. [ ] [proxies](../../../project/本研/pack2/_3info/_4proxies_get.py)：搭建IP池
2. [ ] [file_work](../../../project/本研/pack/_4output/file_work.py)：串联[相关内容](../../../project/本研/README/README.md/#2-问题)
3. [ ] 仍未回复王欣