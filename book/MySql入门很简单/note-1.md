###1-3章不做描述
#第四章：MySql数据类型
##MySql数据类型介绍
###整数类型
![](imgs/20180406-135911.png)

- 每个整数类型都有默认的显示宽度
	- 如果设置了宽度，但是最后插入的值大了，仍可以显示，只要小于默认即可
###浮点数类型和定点数类型
![](imgs/20180406-140423.png)

- MySql可以指定浮点数和定点数的精度
	- 格式：数据类型（M，D）
###日期与时间类型
![](imgs/20180406-140809.png)
###字符串类型
- char类型和varchar类型
![](imgs/20180406-141130.png)
- TEXT类型
![](imgs/20180406-141202.png)
- ENUM类型
	- 在创建表时，enum类型的取值范围就以列表的形式指定了
- SET类型
- 二进制类型
- BLOB类型
##常见问题和解答
![](imgs/20180406-141934.png)
#第五章：操作数据库
##创建数据库
``create database example;``
``show databases;`` 
##删除数据库
``drop database example;``
##数据库存储引擎
<p>存储引擎的概念时MySql的提点，而且时一种嵌入式存储引擎的概念，这决定了MySql数据库中的表可以用不同的方式存储，用户可以根据自己的不同要求，选择不同的存储方式，是否进行事务处理等
###MySQL存储引擎简介
``show engines;``
- 修改默认存储引擎
``default-storage-engine=INNODB``
###InnoDB存储引擎
- 给MySQL提供了事务，回滚，崩溃修复能力和多版本并发控制的事务安全，是一个提供外键约束的表引擎，其处理事务的能力也是超级棒的
- InnoDB存储引擎值中支持自动增长列，且增长列的值不能为空且唯一，自增列必须为主键
- 支持外键。外键所在的表为子表，外键所依赖的表为父表，父表中被子表关联的字段必须为主键
- 创建的表的表结构存储在.fm文件中。数据和索引存储在Innodb_data_home_dir和innodb_data_file_path定义的表空间中。、
- 优缺点：
	- 优：良好的事务管理，崩溃修复恩嗯例和并发控制。
	- 缺：读写效率稍差，占用的数据空间相对比较大
###MyISAM存储引擎
- 曾经时默认存储引擎
- 优点：占用空间小，处理快
- 缺点：不支持事务的完整性和并发性
###MEMORY存储引擎
- 表实际对应一个磁盘文件。默认使用哈希索引。其速度要比使用b树索引快
- 表的处理速度非常快
- 数据易丢失，生命周期短。
![](imgs/20180406-145706.png)
# 第六章：创建，修改和删除表
##创建表
###创建表语法形式
```
create table exp(id int,
				name varchar(20),
				sex boolean
				);
```
- 完整性约束条件表
![](imgs/20180406-165908.png)
###设置表的主键
- 目的：帮助MySQL以最快的速度查找到表中的某一条信息
- 满足的条件：唯一性，非空值
- 单字段主键 :
```
create table exp(stu_id int primary key,
				stu_name varchar(20)
				);
```
- 多主键
```
create table exp2(
		stu_id int,
		course_id int,
		grade float,
		primary key(stu_id,course_id)
		);
```
###设置表的外键
```
 create table exp3(
 				id int primary key,
 				stu_id int,course_id int,
 				constraint c_fk foreign key(stu_id,course_id)
 				references exp2(stu_id,course_id)
 				);
```
###设置表的非空约束
```
 create table exp4(
 				id int not null  primary key,
 				name varchar(20) not null,
 				stu_id int,
 				constraint d_fk foreign key(stu_id)
 				references exp1(stu_id)
 				);

```
###设置表的唯一性约束
```
 create table exp6(
 				id int primary key,
 				stu_id int unique,
 				 name varchar(20) not null
 				 );

```
###设置表的属性值自动增加
```
 create table exp7(
 				id int primary key auto_increment,
 				stu_id int unique,
 				 name varchar(20) not null
 				 );
```
###设置表的属性的默认值
```
 create table exp8(
 				id int primary key auto_increment,
 				stu_id int unique,
 				 name varchar(20) not null
create table exp8(id int primary key auto_increment,
				stu_id int unique,
				 name varchar(20) not null,
				 English varchar(20) not null default 'zero',
				 Math float default 0,
				 computer  float default 0
				 );
```
###查看表结构语句describe
`` describe exp;``
或``desc``
###查看表详细结构语句
```
show create table exp1;
```
##修改表
###修改表名
```
alter table ex rename exp;
```
###修改字段的数据类型
```
alter table tablename modify attributename int;
```
###修改字段名
```
alter table tablename change oldattri newattri newtype;
```
- 只修改字段名
``alter table exp change stu_name  tea_name  oldtype``
###增加字段
``alter table exp add attribute1 type [完整性约束条件] [alter attr2]``
- 表的第一个位置增加字段
``ALTER TABLE  user ADD num INT(8) PRIMARY KEY FIRST``
- 指定位置后增加字段
``ALTER TABLE user ADD address VARCHAR(30) NOT NULL  AFTER phone``
###删除字段
``ALTER TABLE 表名 DROP 属性名``
###修改字段的排列位置
- 字段修改到第一个字段
``ALTER TABLE user MODIFY name VARCHAR(30) first``
- 字段修改到指定位置
``ALTER TABLE user MODIFY sex TINYINT(1) AFTER age;``
###更改表的存储引擎
``ALTER TABLE  user ENGINE=MyISAM;``
###删除表的外键约束
``ALTER TABLE exp DROP FOREIGN KEY c_fk;``
##删除表
###删除没有被关联的普通表
``DROP TABLE exp;``
###删除被其他表关联的父表
``ALTER TABLE exp DROP FOREIGN KEY c_fk;``
``DROP TABLE exp;``
# 索引
##索引简介
###索引的含义和特点
- 是对数据比哦啊中一列或多列的值进行排序的一种结构，提高查询速度
- 两种存储类型：B树索引和哈希索引
- 提高检索速度
- 占用物理空间，耗费创建和维护时间，增删改需要动态维护索引
###索引的分类
- 普通索引
- 唯一性索引
- 全文索引
- 单列索引
- 多列索引
- 空间索引
###索引的设计原子
- 选择唯一性索引
- 为经常需要排序，分组和联合操作的字段建立索引
- 为常作为查询条件的字段建立索引
- 限制索引的数目
-尽量使用数据量少的索引
- 尽量使用前缀来索引
- 删除不再使用或者很少使用的索引
##创建索引
###创建表的时候创建索引
- 创建普通索引
![](imgs/20180407-121351.png)
- 创建唯一性索引
![](imgs/20180407-121432.png)
- 创建全文索引
![](imgs/20180407-121458.png)
- 创建单列索引
![](imgs/20180407-121536.png)
- 创建多列索引
![](imgs/20180407-121601.png)
- 创建空间索引
![](imgs/20180407-121652.png)
###在已存在的的表上创建索引
- 创建普通索引
```
create index index7_id on exp(id);
```
- 创建唯一性索引
```
CREATE UNIQUE INDEX index8_id ON index8(course_id);
```
- 创建全文索引
```
CREATE FULLTEXT INDEX index9_info ON index9(info);
```
- 创建单列索引
```
CREATE  INDEX index10_addr ON index10(address(4));
```
- 创建多列索引
```
CREATE INDEX index11_na ON index9(info);
```
- 创建空间索引
```
CREATE SPATIAL INDEX index12_line ON index12(line);
```
###用ALTER TABLE 语句来创建索引(直接为已存在的表上的一个或几个字段创建索引)
- 创建普通索引
```
ALTER TABLE exp ADD INDEX index13_name(name(20));
```
- 创建唯一性索引
```
ALTER TABLE index14 ADD UNIQUE INDEX index14(course_id);
```
- 创建全文索引
```
ALTER TABLE index15 ADD FULLTEXT INDEX index15_info(infp);
```
- 创建单列索引
```
ALTER TABLE index16 ADD  INDEX index16_info(info);
```
-创建多列索引
```
ALTER TABLE index18 ADD SPTOAL INDEX index18_line(line);
```
##删除索引
- DDROP INDEX 索引名 ON 表名
##常见问题
- MySql中索引，主键和唯一性的区别是什么？
	- 索引简历在一个或者几个字段上，建立后，表中的数据旧按照索引的一定规则排列，这样可以提高查询速度。
	- 主键是表中数据的唯一标识。不同的记录主键值不同。在建立主键时，系统会自动建立一个唯一性索引。
	- 唯一性也是建立在表中一个或者几个字段上。目的时为了对于不同的记录美剧有唯一性
- 表中建立了索引后，导入大量数据为什么会很慢
	- 因为插入一条数据就要对该记录按索引进行排序。解决办法：在没有任何索引的情况插入数据，然后建立索引。
#第八章 视图
##视图简介
- 由数据库中的一个表或多个表到处的虚拟表。作用时方便用户对数据的操作。
###视图的含义
- 是从数据库中一个或多个表中导出的虚拟表。还可以从已经存在的视图的基础上定义。数据库中只存放视图的定义。
###视图的作用
- 使操作简单化（用户角度）
- 增加数据的安全性
- 提高表的逻辑独立性
##创建视图
###在表单上创建视图
```
CREATE VIEW department_view1 AS SELECT * FROM department;
DESC department_view1;
```
###在多表上创建视图
```
CREATE ALGORITHM=MERGE VIEW view1(name,dep,sex,age,address) AS SELECT name,dep.d_name,sex,2009-birthday,address FROM worker dep WHERE worker.d_id=dep.d_id WITH LOCAL CHECK OPTION;
```
##查看视图
###DESC 视图名;
###SHOW TABLE STATUS LIKE ‘视图名’
###SHOW CREATE VIEW 视图名
###SELECT * FROM  views;
##修改视图
###CREATE OR REPLACE ALGORITHM=TEMPTABLE VIEW dep_view(dep,function,location) AS SELECT d_name,function address FROM dep;
###ALTER VIEW dep_view(dep,name,sex,location) AS SELECT d_name,worker.name,worker.sex,address FROPM dep,worker WHERE dep.d_id=worker.d_id WITH CHECK OPTION;
##更新视图
 - 视图更新，都是转换到基本表来更新。只能更新权限范围内的数据
```
UPDATE dep_view SET name='s',function='a';
```
- 以下的几种情况时=是不能更新视图的
	- 视图中包含SUM（），COUNT（），MAX（）和MIN（）函数
	- 视图中包含UNION，UNION ALL，DISTINCT，GROUP BY，HAVING等关键字
	- 常量视图
	- 视图中的SELECT中包含子查询
	- 由不可更新的视图导出的视图
	- 创建视图时，ALGORITHM 为TEMPTABLE类型
	- 视图对应的表上存在没有默认值的列，而且该列没有包含在视图里
- 最好不要对视图更新
##删除视图
```
DROP VIEW IF EXITS view1, vew2;
```
##常见问题
- MySQL中视图和表的区别是什么？
	- 视图是生成的虚拟表
	- 视图不占实际物理空间
	- 建立和删除视图只影响视图本身
	- 视图依赖表存在
	- 一个树图可以对应一个或多个基本表
	- 视图时基本表的抽象，在逻辑意义上简历的新关系
# 第九章：触发器
- MySQL中，触发器执行的顺序是BEFORE触发器，表操作（INSERT，UPDATE ，DELETE）和AFTER触发器
##创建触发器
###只有一个执行语句
```
CREATE TRIGGER trigger BEFORE|AFTER INSERT ON table FOR EACH ROW INSERT INTO trigger_name VALUES(NOW());
```
###多个执行语句的触发器
```
DELIMITER &&
CREATE TRIGGER tri AFTER DELETE ON dep FOR EACH ROW 
	BEGIN 
		INSERT INTO tri_time VALUES('21:01:02');
		INSERT INTO tri_time VALUES('11:11:11');
	END
		&&
DELIMITER; 
```
- begin 和end中有分号，系统默认分号是SQL程序的结束标志，所以我们使用以上结构
##查看触发器
```
SHOW TRIGGERS;
SELECT * FROM table.triggers;
SELECT * FROM table.triggers WHERE TRIGGER_NAME='tr';
```
##触发器的使用
```
CREATE TRIGGER before_insert BEFORE INSERT ON dep FOR EACH ROW INSERT INTO trigger_test VALUES(NULL,''S'');
CREATE TRIGGER after_insert AFTER INSERT ON dep FOR EACH ROE INSERT INTO trigger_test VALUES(NULL,''SDF'');
```
- 在激活触发器时，对触发器中的执行语句存在一些限制。如触发器中不能包含START TRANSACTION ，COMMIT 或ROLLBACK等，也不能有CALL语句。
- 触发器执行时，任何步骤出错都会阻止程序向下执行，但是对于普通表来说，已经更新过的记录时不能回滚的，更新后的数据将继续保存在表中。因此设计触发器要认真考虑
##删除触发器
```
DROP TRIGGER trigger_name;
```


