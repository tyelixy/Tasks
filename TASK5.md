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

     在for循环中修改列表可能导致Python难以跟踪其中的元素（使用while循环代替）

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
   
4. if语句

   1. 条件测试

      相等`==`

      不相等`!=`

      检查多个条件

      * 和     `and`
      * 与     `or`

      > C语言中分别使用`&&`和`||`

      检查特定的值是否在列表中`in`

      检查特定的值是否不在列表中`not in`

   2. if语句

      ~~~python
      if conditional_test:
          do something
      ~~~

      > 条件测试不用`()`包裹，if语句后有`:`，整个语句不包含`{}`,通过缩进确定哪些内容属于if语句内

   3. if-else语句

      ~~~python
      age=17
      if age>=18:
          print("yes")
      else:
          print("no")
      ~~~

      > else后也要加`:`

   4. if-elif-if结构

      ~~~python
      age=18
      if age>18:
          print("yes")
      elif age==18:
          print("on")
      else:
          print("no")
      ~~~

      * else代码可不写
      * 可以根据需要写任意数量的elif语句

      > elif语句前为`elif`而不是`else if`，elif语句条件表达式后有`:`

   5. 处理列表

      * 当列表名用作条件表达式时：若列表中有元素，返回True；若列表为空，返回False

5. 字典

   字典是一系列==键值对==，每一个键都与一个值相关联。

   可以通过键来访问值，与键相关的值可以是任何Python对象

   ~~~python
   pencil={'color':'blue','hardness':'HB','cost':1}
   ~~~

   * 添加键值对

     字典是一种动态结构

     ~~~python
     pencil={}
     pencil['hardness']='HB'
     pencil['color']='blue'
     ~~~

   * 修改字典中的值

     ~~~python
     pencil={'color':'blue','hardness':'HB','cost':1}
     pencil['color']='green'
     ~~~

   * 删除键值对

     ~~~python
     pencil={
         'color':'blue',
         'hardness':'HB',
         'cost':1,#方便添加下一行
     	}
     del pencil['cost']
     ~~~

   * 访问值

     ~~~python
     pencil={'color':'blue','hardness':'HB'}
     print(pencil['color'])
     print(pencil.get('cost','not have'))#括号内为（键，指定键不存在时返回的值）
     ~~~

   * 遍历
   
     ~~~python
     pencil={'color':'blue','hardness':'HB','cost':1}
     for key,value in pencil.items():#items()返回一个键值对列表
         print(f'\nkey:{key}\nvalue:{value}')
     ~~~
   
     可以通过方法`key()`获取字典中所有的键，`value()`获取字典中所有的值
   
6. 用户输入

   ~~~python
   message=input("please input something")
   age=int(input("How old are you?"))
   ~~~

   > 使用函数`input()`获取用户输入，括号内为提示内容
   >
   > 使用`input()`获取的内容为字符串
   >
   > 使用函数`int()`将字符串转为数值

7. while循环

   ~~~python
   num=1
   while num<=5:
       print(num)
       num+=1
   ~~~

   >条件表达式不用`()`包裹，后有`:`，整个语句不包含`{}`,通过缩进确定哪些内容属于while语句内

   * break：跳出循环
   * continue：返回循环开头，根据条件测试结果判断是否继续循环
   
8. 函数

   ~~~python
   def greet_user():#def关键字定义函数
       """显示简单的问候语"""#文档字符串
       print(Hello!)
   ~~~

   > 函数定义语句`()`后有`:`，整个语句不包含`{}`,通过缩进确定哪些内容属于函数内容

   * 传递实参
   
     * 位置实参
   
       ~~~python
       def p_num(num1,num2):
           """打印传入的内容"""
           print(num1)
           print(num2)
       p_num('one','two')#按顺序传入
       ~~~
   
     * 关键字实参
   
       ~~~python
       def p_num(num1,num2):
           """打印传入的内容"""
           print(num1)
           print(num2)
       p_num(num2='one',num1='two')
       ~~~
   
     * 默认值
   
       ~~~python
       def p_num(num1,num2='two'):#有默认值的参数放在后面
           """显示简单的问候语"""
           print(num1)
           print(num2)
       p_num(num1='two')#有默认值的可以不传入
       ~~~
   
     * 传递任意数量的实参
   
       ~~~python
       def p_num(*num):#创建了一个新元组，这样的参数需放在最后
       def p_num2(**num):#创建了一个新字典，这样的参数需放在最后
       n=p_num2(one="1",two="2")
       ~~~
   
   * 返回值
   
     关键词`return`
   
   * 导入
   
     * 导入模块
   
       ~~~python
       import module_name
       ~~~
   
     * 导入特定函数
   
       ~~~python
       from module_name import function_name1,function_name2
       ~~~
   
     * 指定别名
   
       ~~~python
       import module_name as m
       ~~~
   
     * 导入模块中所有函数
   
       ~~~python
       from module_name import *
       ~~~
   
       引用函数时不用加`module.`
   
9. 类

   * 方法`__init__()`

     通过类创建对象时会自动调用这个方法，并传入参数`self`（一个指向实例本身的引用）

     > 构造器？

   * ~~~python
     class Dog:
         def __init__(self,name,age):
             self.name=name
             self.age=age#可以在__init__()方法中对属性赋默认值
     
         def sit(self):
             print(f'{self.name} is sitting.')
         def set_age(self,age):
             if age>0 and age<20:
                 self.age=age
     
     dog=Dog("Willie",6)#创建实例，可以根据需求创建任意数量的实例
     print(dog.age)#直接访问属性
     dog.sit()#调用方法
     dog.set_age(7)#通过方法修改属性
     ~~~

   * 继承

     在既有类的基础上编写新类时，通常要调用父类方法的`__init__()`

     ~~~python
     class Animal:
         def __init__(self,name,age):
             self.name=name
             self.age=age
     
         def sit(self):
             print(f'{self.name} is sitting.')
     class Dog(Animal):
         def __init__(self,name,age):
             """初始化父类属性"""
             super().__init__(name,age)
     #可以增加子类特有的属性和方法，也可以重写父类方法（与父类方法名相同，对参数列表无要求）
     ~~~

   * 导入类（参考导入函数）

10. 文件操作

    ~~~python
    with open('pi_digits.txt') as f:#关键字with在不再需要访问文件后将其关闭
        contents=f.read()#读取文件的全部内容并将其作为字符串赋给contents
    print(contents)#read()到达文件末尾时会返回一个空字符串，print显示空行
    words=contents.split#以空格为分隔符将字符串拆分成多个部分
    
    with open('pi_digits.txt') as f:
    	for line in f:#逐行读取，每行后有换行符
            print(line)
            
    with open('pi_digits.txt','r') as f:#以读取模式打开文件
        lines=f.readlines()#创建一个包含文件各行内容的列表
        
    with open('programming.txt','w') as f:#以只写的方式打开文件（附加模式'a'，读写模式'r+''
        f.write("This is a test.")#写入文件
    ~~~

11. 异常

    ~~~python
    #使用try-except代码块
    try:
    except 异常:
    else:#只有try成功执行后才执行的内容
    ~~~

    

12. 测试

### 面向对象编程（OOP）

> ==以类的方式组织代码，以对象的形式封装数据。==

##### 核心：抽象

##### 三大特性

1. 封装
2. 继承
3. 多态

##### 类和对象

> 从认识论角度考虑：先有对象后有类

__对象__ 是具体的事物，__类__ 是对__对象__的抽象。

> 从代码运行角度考虑：先有类后有对象

__类__是__对象__的模板。

##### 三大特性

* 封装

  * 属性私有

    在属性名前添加`__`

    _（实际上是改变了调用时属性的名字）_

    提供一些可以操作这个属性的方法（get、set方法）

  * 作用

    1. 提高程序安全性，保护数据
    2. 隐藏代码的实现细节
    3. 统一接口
    4. 系统可维护性增加

* 继承

  * 子类是父类的扩展，子类继承父类

  * 继承是类与类之间的一种关系，除此之外还有依赖、组合、聚合等

  * 继承关系的两个类，一个为子类（派生类），一个为父类（基类），

    子类与父类之间，意义上讲应具有“is a”的关系

* * 函数`super()`

    调用父类的属性或方法

* 多态
  * 重写：方法的重写（与属性无关）
    * 重写需要有继承关系，子类重写父类的方法
  * 多态是方法的多态
  * 父类和子类。必须有联系



​      

​      

​      
