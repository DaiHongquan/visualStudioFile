# makrdown语法简介


## 1. [标题](#p1)
使用1~6个 <mark> # </mark>，分别表示1~6级标题，#号后要跟一个空格

## 2. 分割线
***

## 3. 粗体与斜体
**粗体**
*斜体*

## 4. 超链接与图片

## 5. 有序列表
1. 有序列表1
2. 有序列表2

## 6. 无序列表
* 无序列表1
* 无序列表2

## 7. 引用
>这是一段引用

## 8. 行内代码
`
行内代码
`

## 9. 代码块
```java
   System.out.println("hello world");
```

## 10. 流程图
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


```flow
st=>start: Start:>https://www.zybulo.com
io=>inputoutput: verification
op=>operation: Your operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

```
示例:
\```flow
设定
st=>start: Start:>https://www.zybulo.com
io=>inputoutput: verification
op=>operation: Your operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end
流程图
st->io->op->cond
cond(yes)->e
cond(no)->sub->io
\```
```
***
## 11. 公式
$ s = 2 (a + b)$
$$s = 2 (a + b)$$

## 12. 按钮
<kbd>ESC</kbd> + <kbd>SHIFT</kbd> + <kbd>DEL</kbd> 

## 13. 支持部分html标签
\<h1>标签 \<br>标签

## 14. 表格
|居左|居中|居右|
|:--|:--:|--:|
|1|2|3|

## 15. 脚注
脚注[^rootboot]

[^rootboot]:如果没有梦想，和咸鱼有什么区别