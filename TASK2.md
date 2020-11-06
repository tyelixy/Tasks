## 考核期第二阶段

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
   
3. 进入文件
   `cd 文件名`

4. 初始化新的git仓库[^1]
   `git init`

   [^1]:是一个隐藏文件

5. 上传文件

   * 查看文件存储位置

     `git status`

   * 将文件上传至暂存区

     `git add 文件名`

   * 将文件上传到库
   
     `git commit -m '描述'`
     
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
   
6. 删除文件
   * 删除文件
     `rm 文件名`
   
   * 从Git中删除
   `git rm 文件名`
   再提交操作
   
7. 下载项目到本地
   `git clone 地址`
   
   
   