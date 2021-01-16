### 考核期第五阶段

##### 目标

1. 学习Python的基础语法
2. 掌握Python中的数据类型 (学习一些内置的操作函数)
3. ⾯向对象程序设计，学会创建对象，方法定义和调⽤, 掌握面向对象的特性。
4. ⽂件操作

- [推荐] 学会了解使用Python解释器
- [推荐] 了解一些内置函数及类型的实现，说不定能获得新的感悟

##### 笔记

> 会与C语言进行对比。

### Python

#### 基础语法

1. 变量

   每一个变量都指向一个值。

   ~~~Python
   #定义变量
   message="hello world"
   ~~~

   > 不声明数据类型，语句结束没有分号`;`

2. 数据类型

   1. 字符串

      在Python中，用引号（包括单引号`''`和双引号`""`）引起的都是字符串，这使得可以在字符串内包含引号和撇号`'`。

      > 在字符串中写引号和撇号无需转义字符

      * 使用方法修改字符串的大小写

        > 方法是Python可对数据执行的操作

        ~~~Python
        message="hello world"
        print(message.title())#Hello World
        print(message.upper())#HELLO WORLD
        print(message.lower())#hello world
        ~~~

      * 在字符串中使用变量

        ~~~Python
        first_message="hello"
        last_message="world"
        message=f"{first_message.title()} {last_message}"
        #Hello world
        ~~~

      * 删除空白

        ~~~Python
        language=" python "
        print(language.rstrip())#" python"
        print(language.lstrip())#"python "
        print(language.strip())#"python"
        # python
        #python
        #python
        ~~~

   2. 数

      1. 整数

         ~~~Python
         >>>2**3      #乘方运算
         8
         ~~~

      2. 浮点数

         > 任意两个数相除时，结果总是浮点数

      ~~~Python
      #书写很大的数时，可用下划线分组
      num=1_000_000
      print(num) #1000000
      
      #同时给多个变量赋值
      x,y,z=0,0,0
      ~~~

   3. 注释

      > 用`#`标识

3. 列表

   > 用`[]`表示列表，用负数索引可以倒数取出数

   ~~~Python
   nums=[1,2,3,4,5]
   print(nums[-1])#5
   ~~~

   * 修改、添加、删除元素

     ~~~python
     nums=['one','two','three']
     #修改
     nums[0]='zero'
     #添加
     nums.append('four')#添加到列表末尾
     nums.insert(0,'zero')#向指定位置插入元素
     #删除
     del nums[0]
     num1=nums.pop()#弹出末尾元素
     nums.pop(0)#弹出指定索引元素
     nums.remove('three')#通过值删除元素（只能删除第一个指定元素）
     ~~~

   * 组织列表

     ~~~python
     nums=['one','two','three']
     nums.append('four')
     nums.insert(0,'zero')
     #排序
     print(nums)
     print(sorted(nums))#对列表进行临时排序，不会改变列表的原始排序
     print(sorted(nums，reverse=Tree))#按倒序排列
     print(nums)
     nums.sort()#对列表进行永久排序，会改变列表的原始排序
     print(nums)
     #倒着打印列表
     print(nums.reverse())#会改变列表原始排序
     #获取列表长度
     len(nums)
     ~~~

   * 遍历列表

     ~~~python
     #使用for循环遍历数组
     for num in nums:
         print(num)
     ~~~

     > for语句没有大括号`{}`，for语句末尾有冒号`:`，通过缩进判断哪些内容属于for循环内

   * 数值列表

     * 函数range()

       生成一系列数（左闭右开）

       ~~~python
       for v in range(1,5):
           print(v)
       #输出结果    
       #1
       #2
       #3
       #4
       
       #用函数list()将range()结果转换成列表，输出的是一个数字列表
       nums1=list(range(1,6))
       nums2=list(range(1,11,2))#可以指定步长，nums2=[1, 3, 5, 7, 9]
       #列表解析
       squares=[v**2 for v in range(1,11)]#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
       ~~~

     * 简单的统计计算

       ~~~python
       >>>nums=[1,2,3,4,5,6,7,8,9,0]
       >>>min(nums)
       0
       >>>max(nums)
       9
       >>>sum(nums)
       45
       ~~~

   * 切片

     列表的部分元素

     ~~~python
     nums=['one','two','three','four','five']
     print(nums[0:3])#左闭右开
     print(nums[:3])#默认从头开始
     print(nums[-3:])#从倒数第三位开始，到列表末尾结束
     nums2=nums[:]#获得了nums的副本，是两个列表
     ~~~

   * 元组

     值不可变的列表，但对存储元组的变量重新赋值是可以的（重新定义整个元组）

     使用小括号`()`进行标识

     > 严格来说，元组使用逗号`,`而非圆括号`()`进行标识，如果定义只有一个元素的元组，需在这个元素后加上逗号`,`

