## 考核期第二阶段

### git学习笔记

> 分布式版本控制系统

### git命令

在文件夹内右击打开Git Bash

1. 初始化(一次即可)

​      `git config --global user.name 'name'`

​      `git config --global user.email 'email'`

> 可用git config --list检查

2. 创建       

   * 文件夹
   
   ​       `mkdir 文件名`
   
   * 文件
   
     `touch 文件名（包含后缀）`
     文件名若用中文不会显示中文
   
3. 进入文件
   `cd 文件名`

   上一级目录`cd ..`
   
4. 显示当前文件夹

   `pwd`

5. 列出当前文件夹所有文件

   `ls`

6. 移动文件(不能移动文件夹)

   `mv 文件名 文件夹名`

7. 初始化新的git仓库[^1]
   `git init`

   [^1]:是一个隐藏文件

8. 上传文件

   * 查看文件存储位置

     `git status`

   * 将文件上传至暂存区

     `git add 文件名`

     全部提交 `git add .`

   * 将文件上传到库

     `git commit -m '描述'`
     
     上传已跟踪文件（省略git add）
     
     `git commit -am '描述'`
     
     描述中不能含有中文字符。
     
   * 将本地仓库提交到远程
     `git push`

     > 输入用户名、密码
     >
     > > 将config中[remote"orgin"]
     > >
     > > url=https：//github.com/用户名/仓库名.git
     > >
     > > 改为[remote"orgin"]
     > >
     > > url=https：//用户名：密码@github.com/用户名/仓库名.git
     
     授权/直接输入账号密码即可

9. 删除文件（彻底删除）

   * 删除文件
     `rm 文件名`
     
   * 删除文件夹
     
     `rm -r 文件名`
* 从Git中删除
   `git rm 文件名`
   再提交操作
9. 查看更改记录

   `git log`

   若记录过多在出现END后需敲q

   `git log --pretty=online`

2. 返回上个版本

   `git reset --hard HEAD^`

   `git reset --hard HEAD~1`

   `git reset --hard 版本号`

3. 命令记录

   `git reflog`

4. 清屏

   `clear`

13. 查看历史命令

    `history`

14. 撤销修改（删除工作区中的更改）

    `git restore 文件名`

15. 下载项目到本地

    `git clone 地址`

 16. 自定义命令名（未尝试）

 `git config --global alias.自定义 命令`

 大于一个单词的命令需用''引起

14. 下载远程库并合并

    `git pull`

    在对远程库进行更改之后进行，否则`git push`会失败 

15. 标签

    `git tag -a 标签`

    -a：有注释的标签

    关闭编辑器：Esc+Z+Z

    追加标签：`git tag -a 标签 版本号`
    
    查看：`git log --decorate`
    
16. 退出

    `exit`
    
17. 获取ssh密钥

    `ssh-keygen -t rsa`

rsa是加密方式（？）