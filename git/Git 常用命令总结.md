# Git 常用命令总结
##本地仓库

1. 创建版本库

   1. 选择一个合适的地方，创建一个空目录

   2. `git init`：将目录变成可以管理的仓库

   3. ``git add  <file> /git add ``  :文件添加到仓库   把文件放到暂存区
   4. ``git commit -m ``  把文件放到当前分支（版本库）
2. 追溯

   1. ``git status ``：掌握仓库状态

   2. ``git diff <file>``：看看某文件做了什么修改
3. 版本回退
   1. ``git reset --hard commit_id``：版本回退
   2. ``git reflog`` ：查看命令历史，可以帮助回到未来的哪个版本
   3. ``git log ``：查看提交历史，确定回退到哪个版本
   4. ``git reset --hard HEAD^``：回退到上个版本
4. 工作区和暂存区
   1. 工作区：就是我们电脑中看到的目录
   2. 版本库：.git文件
   3. ``git checkout -- file ``：丢弃工作区的修改，其实是用版本库里的版本替换工作区的版本
   4. ``git reset HEAD file``  加上 ``git checkout -- file``   丢弃暂存区的修改+工作区

##远程仓库

由于你的本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置：

1. ``ssh-keygen -t rsa -C "youremail@example.com"``       :创建SSH Key

2. `.ssh`目录，里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

3. 登陆GitHub，打开“Account settings”，“SSH Keys”页面：

   然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴`id_rsa.pub`文件的内容。
###添加远程库

1. github上建库

2. ``$ git remote add origin git@github.com:sscnw/learngit.git``：把本地仓库的内容推送到GitHub仓库。

3. ``git push -u origin master``： 把本地库的所有内容推送到远程库上。

   把本地库的内容推送到远程，用`git push`命令，实际上是把当前分支`master`推送到远程。

   由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

4. 从现在起，只要本地作了提交，就可以通过命令：`` git push origin master``
###从远程库克隆
1. ``$ git clone git@github.com:michaelliao/gitskills.git``

2. Git支持多种协议，包括`https`，但通过`ssh`支持的原生`git`协议速度最快。

