##1. Servlet的生命周期
Servlet有良好的生存期的定义，包括加载和实例化，初始化，处理请求以及服务结束，这个生存期由javax.servlet.Sevlet接口的init(),service() 和destroy()方法表达
Servlet被服务器实例化后，容器运行其init方法，请求到达时运行其service方法，service方法自动派遣运行与请求对应的doGet或doPost方法，当服务器决定将实例销毁的时候调用destroy方法。
## 2. Servlet API中forward() 与redirect()的区别
- 从地址栏来说：
forward是服务器请求资源，服务器直接访问目标地址的URL，把哪个URL的响应内容读取过来，然后把这些内容再发给浏览器，浏览器根本不知道服务器发送的内容从哪里来的，所以它的地址栏还是原来的地址
redirect是服务端根据逻辑，发送一个状态码，告诉浏览器重新去请求哪个地址，所以地址栏显示新的URL，所以redirect等于客户端向服务器发出两次request，同时接收两次response
- 从数据共享来说
forward：转发页面和转发到的页面可以共享request里面的数据
redirect不能共享数据，不仅可以重定向到当前应用程序的其他资源，还可以重定向到同一个站点上的其他应用程序中的资源，甚至是使用绝对URL重定向到其他站点的资源
forward方法只能在同一个web应用程序内的资源之间转发请求，forward是服务器内部的一种操作
redirect是服务器通知客户端，让客户端重新发起请求
所以可以说redirect是一种间接的请求，但是不能说一个请求是属于forward还是redirect
- 从运用的地方说
forward ：一般用于用户登录的时候，根据角色转发到相应的模块
redirect一般用于用户注销登陆时返回主页面和跳转到其他的网站等
- 效率
forward高
redirect低
##3. request.getAttribute()和request.getParameter()有何区别
- request.getParameter()取得是通过容器的实现来取得通过类似post，get等方式传入的数据
	 request.setAttribute()和getAttribute()只是在web容器内部流转，仅仅是请求处理阶段
- getAttribute是返回对象，getParameter是返回字符串
- getAttribute()一向是和setAttribute()一起使用的，只有先用setAttribute()设置之后，才能用getAttribute获得值，它们传递的是Objext类型的数据，而且必须在一个request对象中才有效，而getParameter()是接收表单的get或者post提交过来的参数
##4. JSP静态包含和动态包含的区别
- ``<%@include file="xxx.jsp">``为jsp中的编译指令，其文件的包含是发生在jsp向servlet转换的时期，而``<jsp:include page="xxx.jsp">``是jsp中的动作指令，其文件的包含是发生在编译时期，也就是将java文件编译为class文件的时期
- 使用静态包含只会产生一个class文件，而动态包含会产生多个class文件
- 使用静态包含，包含页面和被包含页面的request对象为同一对象，因为静态包含只是将被包含的页面的内容复制到包含的页面，动态包含包含页面和被包含页面不是同一个页面，被包含的页面的request对象可以渠道的参数范围相对要大一些，不仅可以取到传递到包含页面的参数，同样也能取得在包含页面下传递的参数
##5. MVC各个部分都有哪些技术来实现？如何实现
Model代表的是业务逻辑（通过javabean实现），view是应用大的表示层，由jsp页面产生，controller是提供应用的处理过程控制，一般是一个servlet，通过这种设计模型把应用逻辑，处理过程和显示逻辑分成不同的组件实现，这些组件可以进行交互和重用
##6. JSP有哪些内置对象？(9个)作用分别是什么?
- request 用户端请求，此请求会包含来自get/post请求的参数
- response 网页传回用户端的回应
- pageContext 网页的属性是在这里管理
- session 与请求有关的会话期
- application servlet 正在执行的内容
- out 用来传送回应的输出
- config  servle 的架构不见
- page JSP网页本身
- exception 针对错误页面，未捕捉的例外
##7. Http中，get和post方法的区别
- Get是向服务器索取数据的一种请求，而post是向服务器提交数据的一种请求
- Get是获取信息，而不是修改信息，类似数据库查询功能一样，数据不会被修改
- Get请求的参数会跟在url后进行传递，请求的数据会附在URL之后，以？分割URL和传输数据，参数之间以&相连，%xx中的xx字符为该符号以16进制表示的ascii，如果数据是英文字母/数字，原样发送，如果是空格，转换为+，如果是中文/其他字符，则直接把字符串用base64加密
- Get传输的数据大小有限制，因为get是通过url提交数据，那么get可提交的数据量就跟url的长度有直接关系了，不同的浏览器对url长度的限制是不同的
- get请求的数据会被浏览器缓存起来，用户名和密码将明文出现在url上，其他人可以查到历史浏览记录，数据不太安全，在服务器端，用Request.queryString来获取get方式提交来的数据
- Post请求则作为http消息的实际内容发送给web服务器，数据防止在HTML Header内提交，Post没有限制提交的数据，Post比Get安全，当数据时中文或者不敏感的数据，则用get，因为使用get，参数会显示在地址，对于敏感数据和不是中文字符的数据，则用post
- post表示可能修改服务器上的资源请求，在服务器端，用post方式提交的数据只能用request.form获取
##8. 什么是cookie
cookie是会话技术，将用户的信息保存到浏览器的对象
- cookie数据存放在客户的浏览器上，session放在服务器
- session会在一定时间内保存在服务器上，当访问增多，会比较占用服务器的性能，如果主要考虑减轻服务器性能方面，应当使用cookie
- 单个cookie在客户端的限制是3k，就是说一个站点在客户端存放的cookie不能超过3k
- 将登录信息等重要信息存放在session，其他信息如果需要保留，可以放在cookie
##9 jsp和servlet的区别
- jsp是servlet技术的扩展，本质上就是servlet的简易方式，编译后就是servlet
- 不同点：servlet的应用逻辑是在java文件中，并且完全是从表示层中的html分离出来，而jsp的情况是java和html可以组合成一个扩展名为jsp的文件
- jsp侧重于视图，servlet主要用于控制逻辑，在structs框架中，jsp位于mvc设计模式的视图层，而servlet位于控制层
##10. tomcat容器是如何创建servlet类实例
当容器启动时，会读取在webapps目录下所有的web应用中的web.xml文件，然后对xml文件进行解析，并读取servlet注册信息。然后，将每个应用中注册的servlet类都进行加载，并通过反射的方式进行实例化（有时候也是在第一次请求时实例化）
在servlet注册时加上``<load-on-startup>1</load-on-startup>``如果为正数，则在一开始就实例化，如果不写或者为负数，则第一次请求实例化.
##11. JDBC访问数据库的基本步骤是什么？
- 加载驱动
- 通过DriverManager对象获取连接对象Connection
- 通过连接对象获取会话
- 通过会话进行数据的增删改查，封装对象
- 关闭资源
##12. preparedStatement和Statement的区别
- 效率：预编译会话比普通会话对象高，数据库系统不会对相同的sql语句再次编译
- 安全性：有效的避免sql注入
## 13. 说说事务的概念
- 事务是作为单个逻辑工作单元执行的一系列操作
- 一个逻辑工作单元必须有四个属性，称为原子型，一致性，隔离性，持久性
- conn.setAutoComit(false);设置提交方式为手动提交
- conn.commit()提交事务
- 出现异常，回滚conn.rollback()
##14. 数据库连接池的原理，为什么要用连接池
- 数据库连接是意见费时的事情，连接池可以使多个操作共享一个连接
- 数据库连接池的基本思想就是为数据库连接建立一个“缓冲池”，预先在缓冲池中放入一定数量的连接，当需要建立数据连接时，只需从“缓冲池”中取出一个，使用完毕之后在放回去，我们可以通过设定连接池最大连接数来防止系统无尽的与数据库连接。更为重要的是我们可以通过连接池的管理机制见识数据库连接的数量，使用情况，为系统开发，测试及性能调优提供依据
- 使用连接池是为了提高对数据库连接资源的管理
##15. JDBC的脏读是什么？那种数据库隔离级别能防止脏读
当我们使用事务时，有可能会出现这样的情况，有一行数据刚更新，与此同时另一个查询就读到了这个刚更新的值。这样就导致了脏读，因为更新的数据还没有进行持久化，更新这行数据就是无效的，数据库的TRANSACTIONREADCOMMITTED，TRANSACTIONREAPTEADTABLEREAD和TRANSACTION——SERIALIZABLE隔离级别可以防止脏读
##16. 什么是幻读，哪种隔离级别可以防止幻读
幻读是指一个事务多次执行一条查询返回的却是不同的值，假设一个事务正根据某个条件进行数据库查询，然后另一个事务插入了一行满足这个查询条件的数据，之后这个事务再次执行这条查询，返回结果集中会包含刚刚插入的那条数据，这行新数据被称为幻行，现象叫幻读
只有TRANSACTION——SERIALIZABLE隔离级别才能防止幻读
##17. JDBC的DriverManager是用来做什么的
JDBC的DriverManager是一个工厂类，我们通过它来创建数据库连接，当JDBC的driver类被加载进来时，它会自己注册到DriverManager类里面，然后我们会把数据库配置信息转成DriverManager.getConnection方法
DriverManager会使用注册到它里面的驱动来获取数据库连接，并返回给调用的程序
##18. execute，executeQuery,executeUpdate()的区别是什么
- Statement的execute(String query)方法用来执行任意的SQL语句，如果查询的结果是一个Resultset，这个方法旧返回true。如果结果不是ResultSet，就会返回false，我们可以通过它的getResultSet方法来获取ResultSet，或者通过getUpdateCount()方法来获取更新的记录条数
- Statement的executeQuery(String query)接口用来执行select查询，并且返回ResultSet，即使查询不到记录返回的ResultSet也不会为null，我们通常使用executeQuery来执行查询语句，这样的话如果传进来的是insert或者uodate，它会抛出异常
- Statement的executeUpdate(String query)方法用来执行insert或者update/delete（DML）语句，或者什么也不返回，对于DDL语句，返回值是int类型，如果是DML语句的话，它就是更新的条数，如果是DDL的话，旧返回0
只有当你不确定是什么语句的时候才应该用execute方法，否则应该使用executeQuery或者executeUpdate方法
##19. SQL查询出来的结果分页显示一般怎么左
Mysql
```
select * from students limit " + pageSize*(pageNumber-1)+","+pageSize;
```
##20. JDBC的ResultSet是什么
在查询数据库后会返回一个ResultSet，它就像是查询结果集的一张数据表
ResultSet对象维护了一个游标，指向当前的数据行，开始的时候这个游标指向的是第一行，如果调用了ResultSet的next方法后游标会移动下一行，如果没有更多数据，旧返回false，可在for循环中遍历数据集
默认的resultset是不能更新的，游标也只能往下移。也就是说你只能从第一行到最后一行遍历以便，不过也可以创建可以回滚或者可更新的resultset
当生成resultset的statement对象要关闭或者重新哦你执行或是获取下一个resultset的时候，resultset对象也会自动关闭
可以通过resultset的getter方法，传入列名或者从1开始的序号来获取列数据 