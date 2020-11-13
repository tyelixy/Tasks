## 考核期第一阶段

### Markdown学习笔记

> 轻量级标记语言
>
> > 是一类用简单句法描述简单格式的文本语言
>
> 允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML/HTML文档

### 常用语法

#### 一、纯文本部分

##### 1、标题

行首加入1-6个#，分别表示1-6阶标题内容和行首的#间需有一个空格。

即

```c
# 第一阶标题
## 第二阶标题
### 第三阶标题
#### 第四阶标题
##### 第五阶标题
###### 第六阶标题
```

# 第一阶标题
## 第二阶标题
### 第三阶标题
#### 第四阶标题
##### 第五阶标题
###### 第六阶标题

##### 2、字体

1. 加粗：在需要加粗的内容前后分别加**或__

   ~~~c
   **加粗**
   __加粗__
   ~~~

   **加粗**
   __加粗__

2. 倾斜：在需要倾斜的字体前后加*或_

   ~~~c
   *倾斜*
   _倾斜_
   ~~~

   *倾斜*
   _倾斜_

3. 加粗倾斜：字体前后分别加***或___

   ```c
   ***加粗倾斜***
   ___加粗倾斜___
   ```

   ***加粗倾斜***
   ___加粗倾斜___

4. 删除线:内容两边加~~

   ~~~c
   ~~删除线~~
   ~~~

   ~~删除线~~
   

##### 3、分割线

用三个以上*或-或_

_符号之间可以有空格，*和-中间有空格可能引起歧义。

~~~c
---
__ _
* * *
~~~

---
__ _
* * *



##### 4、引用

将>置于段首即可

~~~c
>内容
内容
    
或

>内容
>内容
~~~

>内容<br/>
>内容<br/>

>内容<br/>
>内容<br/>

引用可以嵌套

~~~c
>text
>>text
~~~

>text
>
>>text

##### 5、列表

1. 无序列表

   在内容前加-或+或*

   ~~~c
   - 内容
       
   + 内容
       
   * 内容     
   ~~~

   * 内容

   + 内容
     

   * 内容   

   无序列表可以嵌套 ，上下级之间需有空格。

   ~~~c
   - 内容
     + 内容
   ~~~

   - 内容

     + 内容

2. 有序列表

   阿拉伯数字加上.再加空格，输入的数字并不影响有序列表前的数字。

   ~~~c
   1. 内容
   8. 内容
   
   ~~~

   1. 内容
   8. 内容

   有序列表也可以嵌套。

##### 6、表格

~~~c
| 标题 | 标题 | 标题 |
| ---- | :--: | ---: |
| 内容 | 内容 | 内容 |
~~~

| 标题 | 标题 | 标题 |
| ---- | :--: | ---: |
| 内容 | 内容 | 内容 |

:--:表示居中

---：表示右对齐

#####  7、代码块

1. 三个`或三个~加语言：

~~~c
//```c
//~~~java
~~~

```c

```

~~~java

~~~

2. 单行代码，将内容用`包起来：

   ~~~c
   //`代码内容`
   ~~~

`代码内容`

3. 制表符/四格空格

       内容
   

##### 8、脚注

脚注中的链接可以跳转。

~~~c
内容[^1]
[^1]:脚注
~~~

内容[^1]

内容[^2]

[^1]:脚注
[^2]:https://www.bilibili.com/

##### 9、排版

首行缩进

1. 缩进一个中文字符：在文字前加`&emsp;`

   &emsp; 一段内容

2. 缩进半个中文字符：在文字前加`&ensp;`

   &ensp;一段内容

3. 缩进四分之一个中文字符：在文字前加`&nbsp;`

   &nbsp;一段内容





#### 二、插入链接

##### 1、插入图片

1. 本地图片

   `![图片](地址)`

   ![图片](zs7.png)
   
   本地图片可上传至GitHub后使用链接。
   也可以与.md文件放在同一位置下以置入图片。
   
2. 图片链接

   `![图片](网址)`

   ![图片](https://bkimg.cdn.bcebos.com/pic/ca1349540923dd54564e7c084a40a4de9c82d158e233?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxNTA=,g_7,xp_5,yp_5)
   
   `![mingzi][biaoqian]`
   
   `[biaoqian]:网址`
   
   ![tupian][id]
   
   [id]:https://bkimg.cdn.bcebos.com/pic/ca1349540923dd54564e7c084a40a4de9c82d158e233?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxNTA=,g_7,xp_5,yp_5
   
   

##### 2、超链接

   1. `[名字](链接)`

      [百度](https://www.baidu.com/)

   2. `<网址>`

   <https://www.baidu.com/>

   3. `[MINGZI][BIAOQIAN]`

      `[BIAOQIAN]:网址`

[BAIDU][1]

[1]:<https://www.baidu.com/>

   

4. `[baidu][]`

​       `[baidu]:网址`

[baidu][]

[baidu]: <https://www.baidu.com/>



#### 三、使用HTML标签

##### 1、更改字体、大小、颜色

~~~html
<font face="黑体">黑体</font>
<font color=red>红色</font>
<font color=#008000>绿色</font>
<font color=Blue>蓝色</font>
<font size=5>尺寸</font>
<font face="黑体" color=#008000 size=5>内容</font>
~~~

<font face="黑体">黑体</font>
<font color=red>红色</font>
<font color=#008000>绿色</font>
<font color=Blue>蓝色</font>
<font size=5>尺寸</font>
<font face="黑体" color=#008000 size=5>内容</font>

##### 2、添加文字背景色

   ~~~html
   <table><tr><td bgcolor=yellow>背景色黄色</td></tr></table>
   ~~~

<table><tr><td bgcolor=yellow>背景色黄色</td></tr></table>

##### 3、文字对齐

   ~~~html
   <center>居中
   <p align="left">左对齐
   <p align="right">右对齐
   ~~~
<center>居中
<p align="left">左对齐
<p align="right">右对齐

##### 4、加入上下标

`H<sub>2</sub>O`

`X<sup>2</sup>`

H<sub>2</sub>O              X<sup>2</sup>
