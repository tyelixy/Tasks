### 考核期第三阶段

### HTML

> 超文本标记语言
>
> > 不是编程语言
> >
> > 是一套标记标签
>
> 用标记标签描述网页

##### 一、关于HTML文档

> 包含了HTML标签和文本内容
>
> 也叫web页面

##### 二、关于HTML标签

> 用尖括号`<>`包围的**关键词**
>
> 通常成对出现`<></>`
>
> > 第一个是开始标签（开放标签）
> >
> > 第二个是结束标签（闭合标签）

##### 三、关于HTML元素

> 通常与HTML标签描述同样的意思
>
> 但严格来说包含了开始标签与结束标签
>
> 大多数 HTML 元素可以嵌套

##### 四、HTML网页结构

```html
<html>
    <head>
        <title>页面标题</title>
    </head>
    <body>
        <h1>    标题    </h1>
        <p>
            段落
        </p>
    </body>
</html>
```

其中<body>区域内的部分在网页内显示，title在网页上方标题位置显示。

1. 标签：

   > HTML 标题标签**只用于标题**
   >
   > 用标题可以呈现文档结构
   >
   > 搜索引擎使用标题为网页的结构和内容编制索引

##### 五、声明

1. `<!DOCTYPE>`

   声明HTML的版本（不区分大小写，HTML标签对大小写不敏感）。

   例如：

   HTML 5:`<!DOCTYPE HTML>`

2. 声明字符

   可用于进行中文编码：`<meta charset="UTF-8"`

   > 在头部将字符声明为UTF-8或GBK(Chinese Internal Code Specification,即`汉字内码扩展规范`)

##### 六、HTML属性

>HTML 元素可以设置属性（对大小写不敏感，但推荐用小写）
>属性可以在元素中添加__附加信息__
>属性一般描述于__开始标签__

属性值应该始终被包括在引号内(一般为双引号`""`,在属性值内含有双引号时使用单引号`''`)。

`属性=""`

举例：

```html
class \\为HTML元素定义类名
id    \\定义元素的唯一id
style \\规定元素的行内样式
title \\描述了元素的额外信息
```



##### 七、HTML语法

1. 换行：`<br>`或`<br/>`

   > 屏幕的大小，以及对窗口的调整都可能导致HTML被显示的不同的结果。
   > 当显示页面时，浏览器会**移除源代码中多余的空格和空行**。**所有连续的空格或空行都会被算作一个空格**，无法通过在 HTML 代码中添加额外的空格或换行来改变输出的效果。
   > 需要注意的是，HTML 代码中的**所有连续的空行（换行）也被显示为一个空格**。

2. 水平线：`<hr>`

3. 注释：`<!--  注释 -->`

4. 斜体：`<i>文字</i>`

5. 加粗：`<b>文字</b>`

6. 上标和下标：`<sup>上标</sup>``<sub>上标</sub>`

7. `<code>`标签:`<code></code>`

   > 用于表示计算机源代码或者其他机器可以阅读的文本内容
   >
   > 通常只是把文本变成等宽字体，但它暗示着这段文本是**源程序代码**

8. 突出重要：

   `<strong></strong> ` ：效果同<b>

   `<em></em>`:效果同<i>

###### HTML头部

`<title>`

* 在HTML文件中是必须的
* 定义文档标题
* `<title>文档标题</title>`

`<base>`              ?

* 描述基本链接地址/链接目标
* 作为HTML文档中所以链接标签的默认链接
* `<base> herf="网址" </base>`

`<link>`               ?

* 定义文档与外部资源的关系
* `<link rel="" type="" href="">`

`<style>`

* 定义HTML文档的样式文件引用地址
* 也可以直接添加样式
* `<style type="">内容</style>`

`<meta>`

* 描述一些基本的元数据（并不显示在页面上，但会被浏览器解析）

`<script>`

* 用于加载脚本文件

###### 主体部分

1. 链接

   链接：`<a href="网址">链接文本</a>`

   > 其中`href`为属性

   链接文本可以是**文本**、**图片**或**其他HTML元素**。

   * target属性：定义被链接的文档在何处显示

     ```html
     <a href="网址" target="_blank" >链接文本</a>       <!-- 在新窗口打开文档 -->
     ```


   锚链接`href="#锚标记"`

   * 实现页面内跳转（到相应位置）

2. 图像：定义`<img src="url" alt="some_text">`    

     `<img src="图片路径" width="宽”  height=“高”>`

   属性：

   * src：source，即源属性，值为图像的URL地址,URL 指存储图像的位置。
   * alt：alt 属性用来为图像定义一串预备的可替换的文本。当浏览器无法显示图像时将显示该文本。
   * width，height：设置图片的宽和高。
   * title：鼠标悬停时显示文字
   
3. 表格：定义`<table border="">`

     ```html
        <table border="1">
            <tr>
                <th>header 1</th>
                <th>header 2</th>
            </tr>
            <tr>
                <td>1,1</th>
                <td>1,2</th>
            </tr>
            <tr>
                <td>2,1</th>
                <td>2,2</th>
            </tr>
        </table>
     ```
     标签

     * `<th>`：定义表头，显示为粗体居中文本
     * `<td>`：定义表格内容，默认左对齐
     * `<tr>`：依次定义表格的每一行

     属性：

     * border:规定表格边框的宽度（为0则无边框）

       > 可不规定边框，通过css来设置边框的样式和颜色
       
     * colspan：跨列

     * rowspan：跨行

4. 列表

     1. 有序列表：定义`<ol><li>项</li></ol>`

     2. 无序列表：定义`<ul><li>项</li></ul>`

        标签：`<ul>`

        * `<li>`:定义每一项的内容

     3. 自定义列表：定义`<dl><dt>项</dt><dd></dd></dl>`

        标签：`<dl></dl>`

        * `<dt>`：项开头
        * `<dd>`：项内容

5. 区块

     HTML可以通过`<div>`和`<span>`将元素组合起来

     > 区块元素
     >
     > > 块级元素：__显示__时常以新行开始&结束
     >
     > > 内联元素：__显示__时通常不以新行开始

     `<div>`：【块级元素】没有特定含义，可用于对文档布局，与css一起使用可以对大的内容块设置样式属性

     > 用于文档布局可以代替`<table>`

     `<span>`：【内联元素】没有特定含义，与css一起使用可以为部分文本设置样式属性

6. 表单：表单用于向服务器传输数据

     标签：`<form></form>`

     * `<input>`

     * `<textarea>`：文本域（cols，row）

     * `<label for="id">`(增强鼠标可用性)

     * `<select>`：下拉框(默认值通过selected设置)

       * `<option>`【项】

       属性：

       * type：定义输入类型
       
         > 输入类型
         >
         > > 文本域`text`
         > >
         > > 密码字段`password`
         > >
         > > 搜索框`search`
         > >
         > > 单选按钮`radio`（必须有value，需要name；通过checked设置默认值）
         > >
         > > 复选框`checkbox`（通过checked设置默认值）
         > >
         > > 提交按钮`submit`
         > >
         > > 重置`reset`
         > >
         > > 按钮：`bottom`;
         > >
         > > ​           `image`(作用同submit)
       
       * name：规定表单名称，提供引用方法
       
       * placeholder：框中显示内容
       
       * value：提交按钮显示内容/默认初始值
       
       * file：文件域
       
       * action：表单提交的位置，可以是网站，也可以是请求处理地址
       
       * method：表单提交方式get(可以在URL中看到提交信息）/post（在url中看不到提交信息，可以传输大文件）
       
       * readonly：只读
       
       * disabled：禁用
       
       * hidden：隐藏域
       
       * placeholder：提示信息
       
       * required：必须填写
       
       * pattern：正则表达式

7. 按钮：`<button>显示</button>`

8. 引用：`<blockquote>引用</blockquote>`                   ?

9. 注释：`<abbr title="注释">内容</abbr>`

10. 框架：定义`<iframe src="url"></iframe>`

      > 实现在同一个浏览器窗口中显示不止一个页面

      属性：

      * 宽width：可以是像素也可以是比例
      * 高height：可以是像素也可以是比例
      * 源src
      * frameborder ：用于定义iframe表示是否显示边框。

      >iframe可以显示一个目标链接的页面(在框架内显示网页)
      目标链接的target属性必须使用iframe的name属性

      8. 关于颜色

         属性：

         * `rgb(r,g,b)`：代表红、绿、蓝三种颜色的组成（每一项取值位于0~255，十六进制00~FF）

         * `rgba(r,g,b,a)`：在rgb基础上增加了alpha通道（取值为0~1）

           

         * 有141个颜色名称是在HTML和CSS颜色规范定义的（17标准颜色，再加124）
         
         * 颜色值由十六进制来表示红、绿、蓝（RGB）。
         十六进制值的写法为 # 号后跟三个或六个十六进制字符。
           三位数表示法为：#RGB，转换为6位数表示为：#RRGGBB。
         
      9. 脚本：

         标签：`<script></script>`:定义客户端脚本（如JavaScript）

         * 可以包含脚本语句
         * 可以通过源属性（src）指向外部脚本文件

         ​            `<noscript></noscript>`：提供无法使用脚本时的替代内容（可以包含普通HTML页面中能找到的所有元素）

      10. 字符实体（对大小写敏感）：为了正确显示预留字符（如<>)

          实体名称后需加`;`
          
          | 实体名称  | 描述                         |
          | --------- | ---------------------------- |
          | `&nbsp`   | 不间断空格，用于显示多个空格 |
          | `&lt`     | 小于号<                      |
          | `&gt`     | 大于号>                      |
          | `&amp`    | 和&                          |
          | `&quot`   | 引号"                        |
          | `&apos`   | 撇号&apos;                   |
          | `&times`  | 乘号&times;                  |
          | `&divide` | 除号&divide;                 |
          
      11. HTML   URL                    ?

          URL是一个网页地址，可以是网址域名或互联网协议（IP）地址

          网页地址语法规则：`scheme://host.domain:port/path/filename`

          * scheme：定义因特网服务类型

            * http：超文本传输协议
            * https：安全超文本传输协议
            * ftp：文件传输协议
            * file：本地文件

          * host ： 定义域主机

            > http 的默认主机是 www

          * domain ：定义因特网域名

          * :port：定义主机上的端口号

            > http 的默认端口号是 80

          * path：定义服务器上的路径

            > 如果省略，则文档必须位于网站的根目录中

          * filename：定义文档/资源的名称

          URL 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。
           URL 不能包含空格。URL 编码通常使用 + 来替换空格。

      12. 视频和音频

          * `<video src="" controls></video>`

          * `<audio src="" controls></video>`

            属性：

            * controls：控制按钮
            * src：源
            * autoplay：自动播放


### CSS

> 用于渲染HTML元素标签的样式

##### 使用方法(样式表)

* 内联样式：在HTML元素中使用`<style>`属性
  * 应用到个别元素
  * `<元素名 style="">`
  
* 内部样式表：在HTML头部用`<style>`元素来包含CSS
  * 应用于单个文件
  * `<style type="text/css"></style>`
  
* 外部引用：使用外部CSS文件
  * 应用到多个页面
  * `<link rel="stylesheet" type="text/css" href="文件名.css">`
  * 每个页面使用 <link> 标签链接到样式表。<link> 标签在（文档的）头部
  * 浏览器从“文件名.css”中读取样式声明并根据它来格式文档。该文件不能包含任何HTML标签。
  
* 多重样式

  >如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来。 

  > 内联样式> 内部样式>外部样式 > 浏览器默认样式
  >
  > 如果外部样式放在内部样式的后面，则外部样式将**覆盖**内部样式。

### css规则

#### 选择器：

需要改变样式的HTML元素

* id选择器

> id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。（一般仅有一个）

> HTML元素以id属性来设置id选择器（跟在标签名后，`>`前）
>
> CSS 中 id 选择器以 "#" 来定义（在`<style>`标签内

* class选择器

  > class 选择器用于描述**一组元素**的样式（用大括号`{}`括起），class 选择器有别于id选择器，class可以在多个元素中使用

  > class 选择器在HTML中以class属性表示（跟在标签名后，`>`前）
  >
  > 在 CSS 中，类选择器以一个点"."号显示

#### 一条/多条声明：

每条声明以分号`;`结束，整体以大括号`{}`括起

* 属性：样式属性
* 值：属性的值，与属性被冒号`:`分开

##### 背景

| 属性                  | 说明                            | 例子                                                    |
| --------------------- | ------------------------------- | ------------------------------------------------------- |
| background-color      | 设置背景颜色                    | h1 {background-color:#6495ed;}                          |
| background-image      | 设置背景图                      | body {background-image:url('paper.gif');}               |
| background-repeat     | 背景图水平或垂直平铺或不平铺    | background-repeat:repeat-x;background-repeat:no-repeat; |
| background-attachment | 背景图固定/随着页面其余部分滚动 | background-attachment: fixed;(固定的背景图像)           |
| background-position   | 改变图像在背景中的位置          | background-position:right top;                          |

为了简化这些属性的代码，可以将这些属性合并在同一个属性中：body {background:#ffffff url('img_tree.png') no-repeat right top;}

（依照上表顺序）

##### 文本格式

| 属性            | 说明                       | 例子                                                         |
| --------------- | -------------------------- | ------------------------------------------------------------ |
| color           | 颜色                       | body {color:red;}<br/>h1 {color:#00ff00;}<br/>p.ex {color:rgb(0,0,255);} |
| text-align      | 对齐方式                   | h1 {text-align:center;}<br/>p.date {text-align:right;}<br/>p.main {text-align:justify;}（每一行被展开为宽度相等，左，右外边距是对齐） |
| text-decoration | 文本修饰                   | a {text-decoration:none;}（删除链接下划线）<br/>h1 {text-decoration:overline;}<br/>h2 {text-decoration:line-through;}<br/>h3 {text-decoration:underline;} |
| text-transform  | 指定一个文本中的大小写字母 | p.uppercase {text-transform:uppercase;}(全部大写）<br/>p.lowercase {text-transform:lowercase;}（全部小写）<br/>p.capitalize {text-transform:capitalize;}（单词首字母大写） |
| text-indent     | 指定文本的第一行的缩进     | p {text-indent:50px;}                                        |

##### 字体

| 属性        | 说明                                           | 例子                                                         |
| ----------- | ---------------------------------------------- | ------------------------------------------------------------ |
| font-family | 字体（字体系列的名称超过一个字，它必须用引号） | p{font-family:"Times New Roman", Times, serif;}<br/>（设置几个字体名称作为一种"后备"机制） |
| font-style  | 字体样式                                       | p.normal {font-style:normal;}（正常）<br/>p.italic {font-style:italic;}（斜体）<br/>p.oblique {font-style:oblique;}（倾斜） |
| font-size   | 字体大小（可填像素，em，百分比）               | h1 {font-size:40px;}                                         |

> 用em代替像素:
>
> 1em和当前字体大小相等，在浏览器中默认的文字大小是16px，因此，1em的默认大小是16px。

##### 链接

属性：

* a:link - 正常，未访问过的链接
* a:visited - 用户已访问过的链接
* a:hover - 当用户鼠标放在链接上时
* a:active - 链接被点击的那一刻

可以设置背景颜色，字体颜色，进行文本修饰等。

##### 列表

属性：

* list-style-type:

  | 有序                    | 无序   |
  | ----------------------- | ------ |
  | upper-roman（罗马数字） | circle |
  | lower-alpha（小写字母） | square |

* list-style-image: url()

  指定列表项标记的图像

##### css盒子模型

![盒子模型](https://www.runoob.com/images/box-model.gif)

* Margin——外边距【透明】

  两个盒子靠在一起外边距取大的。

* Border——边框

* Padding——内边距【透明】

* Content——内容（宽度通过width设置）

1. 边框

   属性：

   * 边框宽度：border-width
     * 具体值（单位px或em）
     * 关键字：think，dium，thin（具体宽度可自定义）

   * 边框样式：border-style

     * none（无）
     * dotted（虚线）
     * solid（实线）
     * double（两个边框，宽和border-width相同）
     * [其他](https://www.runoob.com/try/try.php?filename=trycss_border-style)

     可有1-4个值

     可以单独设置各边（top/right/bottom/left）

   * 边框颜色：border-color

     > 需要先设置边框样式

### css注释

/* 注释*/