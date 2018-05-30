# Nginx初探（一）：Mac下Niginx 安装

```
以一个小白的身份对nginx进行学习，欢迎大家相互分享和指正！
```

### nginx安装（Mac）：

1. 安装brew：

    - 在命令行直接输入`brew`就可以查看是否安装过brew

   - 如果没有安装

     `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. 安装nginx(命令行输入)

   - brew update    

   - brew search nginx    //查询安装软件是否存在

   - brew install nginx    //安装nginx

     ![nginx_1](/Users/ssc/Project/git_rep/basic-note/daily-note/images/nginx_1.png)

   - nginx    //输入后没有任何输出就说明成功了，没有坏消息就是好消息

     ![nginx_2](/Users/ssc/Project/git_rep/basic-note/daily-note/images/nginx_2.png)

   - 在网页地址栏输入localhost：8080

   - 成功页面

     ![nginx_3](/Users/ssc/Project/git_rep/basic-note/daily-note/images/nginx_3.png)