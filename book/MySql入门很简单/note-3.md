#第15章：MySQL用户管理
##权限表
- 安装MySQL时会自动安装一个名为mysql的数据库，mysql数据库下面存储的都是权限表，用户登录后，MySQL数据库系统会根据这些权限表的内容为每个用户赋予响应的权限。这些权限表中最重要的时user表，db表和host表
###user表
- 用户列
	- 包括Host：主机名，User：用户名，Password：密码
- 权限了列

	