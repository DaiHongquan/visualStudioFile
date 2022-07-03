
# Markdown语法简介

&copy;代宏全 2022.1.1-2099.1.1

Markdown 是一种轻量级标记语言，是一种书写的格式，能将文本换成有效的XHTML(或者HTML)文档、PDF、WORD等，语法简洁明了，易于掌握，所以用它来写作是件既效率又舒服的事情。Markdown 的理念是，能让文档更容易读、写和随意改。prince不支持流程图，首页带水印;chrome pdf 代码框没有样式，不支持强调标记;markdown pdf 不支持流程图、脚注、\<kbd>。最好是open in browser,然后点击打印，另存为pdf，页眉页脚样式没修改前，最好不显示页眉页脚。






<h1 id="menu">导航</h1>

## 壹.[标题](#p1)

## 贰.[分割线](#p2)

## 叁.[斜体和粗体](#p3)

## 肆.[超链接和图片](#p4)

## 伍.[无序列表](#p5)

## 陆.[有序列表](#p6)

## 柒.[文字引用](#p7)

## 捌.[行内代码](#p8)

## 玖.[代码块](#p9)

## 拾壹.[流程图](#p10)

## 拾壹.[表格](#p11)

## 拾贰.[数学公式](#p12)

## 拾叁.[支持HTML标签](#p13)

## 拾肆.[按钮](#p14)

## 拾伍.[脚注](#p15)
---


<h2 id="p1">壹.标题</h2>

标题使用 <mark> #+空格+标题名 </mark>，1~6个 <mark> # </mark>分别对应 <mark> h1~h6 </mark>

```
# 标题名
示例：
## 壹.标题
```
---



<h2 id="p2">贰.分割线</h2>

分割线使用三个 <mark> - </mark> 或 <mark> * </mark> 字符

```
示例：
---
***
```
---



<h2 id="p3">叁.斜体和粗体</h2>

*斜体* 使用一个 <mark> * </mark>

**粗体** 使用两个 <mark> * </mark>
```
示例：
*斜体*
**粗体**
``` 
---



<h2 id="p4">肆.超链接和图片</h2>

超链接使用 <mark> \[超链接名字](url) </mark>
[百度一下，你就知道](https://www.baidu.com/) 

图片使用 <mark> \!\[超链接名字](url) </mark>
![图片加载失败](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%253A%252F%252Fdingyue.ws.126.net%252F2021%252F0314%252F94ad46dbj00qpy1do0021d200rs00rsg008t008t.jpg%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg&refer=http%3A%2F%2Fnimg.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1656826971&t=99b55df3a8d9b4cf743028bcd9cb3e2d)

```
[超链接名字](url) 
![图片加载失败时描述](url) 
示例： 
[百度一下，你就知道](https://www.baidu.com/)
![图片加载失败](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%253A%252F%252Fdingyue.ws.126.net%252F2021%252F0314%252F94ad46dbj00qpy1do0021d200rs00rsg008t008t.jpg%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg&refer=http%3A%2F%2Fnimg.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1656826971&t=99b55df3a8d9b4cf743028bcd9cb3e2d)
```
---



<h2 id="p5">伍.无序列表</h2>

无序列表使用 <mark> *+空格+列表项 </mark>
* 无序列表1
* 无序列表2
    * 无序列表1
    * 无序列表2

```
* 列表项
示例： 
* 无序列表1
* 无序列表2
    * 无序列表1
    * 无序列表2
```
---



<h2 id="p6">陆.有序列表</h2>

有序列表使用 <mark> 序号+.+空格+列表项 </mark>
1. 有序列表1
2. 有序列表2
   1. 有序列表1
   2. 有序列表2

```
数字. 列表项
示例： 
1. 有序列表1
2. 有序列表2
   1. 有序列表1
   2. 有序列表2
```
---



<h2 id="p7">柒.文字引用</h2>

文字引用使用 <mark> >+引用文字 </mark>
> 这是一段引用文字

```
>引用文字
示例： 
>这是一段引用文字
```
---



<h2 id="p8">捌.行内代码</h2>

行内代码使用 <mark> \`+代码+\` </mark>

`
print(1);
`

```
`
代码
`
示例： 
`
print(1);
`
```
---



<h2 id="p9">玖.代码块</h2>

代码块使用 <mark> \`\`\`+语言+\`\`\` </mark>
```java
public class Hello {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        //带回车（换行）的输出
		System.out.println("helloworld");
	}
}
```

```java
示例：
\```java
public class Hello {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        //带回车（换行）的输出
		System.out.println("helloworld");
	}
}
\```
```
---



<h2 id="p10">拾.流程图</h2>

主要的语法为 name=>type: describe，其中 type 主要有以下几种：
1. 开始和结束：start end
2. 输入输出：inputoutput
3. 操作：operation
4. 条件：condition
5. 子程序：subroutine

```flow
st=>start: 开始
io=>inputoutput: 输入输出
op=>operation: 操作
cond=>condition: 条件
sub=>subroutine: 子程序
e=>end: 结束

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

```
示例:
\```flow
设定
st=>start: 开始
io=>inputoutput: 输入输出
op=>operation: 操作
cond=>condition: 条件
sub=>subroutine: 子程序
e=>end: 结束
流程图
st->io->op->cond
cond(yes)->e
cond(no)->sub->io
\```
```
---



<h2 id="p11">拾壹.表格</h2>

表格使用 多个竖线 <mark> | </mark>，
表头 用居左居右等分隔 居左 <mark> :-- </mark> 居中 <mark> :--: </mark> 居右 <mark> --: </mark>,冒号在哪里就是居哪里
|居左|居中|居右|
|:--|:--:|--:|
|1|2|3|

```
|表头1|表头2|表头3|
|:--|:--:|--:| 
|1|2|3|
示例： 
|居左|居中|居右|
|:--|:--:|--:|
|1|2|3|
```
---



<h2 id="p12">拾贰.数学公式</h2>

用美元符号 <mark> $ </mark>包裹,两个美元符号表示单占一行, <mark>\$公式\$ </mark>

公式 $ \sum_{i = 0}{n}\frac{1}{i2} $

独占一行公式 $$ \sum_{i = 0}{n}\frac{1}{i2} $$

```
示例： 
公式 $ \sum_{i = 0}{n}\frac{1}{i2} $
独占一行公式 $$ \sum_{i = 0}{n}\frac{1}{i2} $$
```
---



<h2 id="p13">拾叁.支持HTML标签</h2>

支持少部分HTML标签
例如换行 <mark> \<br> </mark>、标题 <mark> \<h1> </mark>等

```
换行 <br>、标题 <h1>等
示例： 
换<br>行
<h1>标题</h1>
```
---



<h2 id="p14">拾肆.按钮</h2>

按钮使用 <mark> kbd </mark> 标签
按 <kbd> CTRL </kbd> + <kbd>SHIFT</kbd> + <kbd>ESC</kbd> 启动任务管理器

```
<kbd>标签
示例： 
按 <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>ESC</kbd> 启动任务管理器
```
---



<h2 id="p15">拾伍.脚注</h2>

脚注使用 <mark> \[^脚注名字] </mark> 然后在文档末尾加上 <mark> \[^脚注名字]：脚注内容 </mark>

这是一个脚注[^rootnote]

同样，超链接也能使用此种写法，只需要去掉 <mark> ^ </mark>符号

```
示例
这是一个脚注[^rootnote]
[^rootnote]:如果没有梦想，和咸鱼有什么区别
```
---



[回到目录](#menu)

[^rootnote]:如果没有梦想，和咸鱼有什么区别