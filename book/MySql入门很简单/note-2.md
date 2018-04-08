#第十章：查询语句
##基本查询语句
```
SELECT num,name,age FROM emp;
SELECT num,address FROM emp WHERE age>23 ORDER BY d_id DESC;
//ORDER BY 表示排序方式 默认ASC 升序
```
##单表查询
###查询所有字段
```
SELECT num,id address,age FROM emp;
SELECT * FROM emp;
```
###查询指定字段
```
SELECT num FROM emp;
```
###查询指定记录
```
SELECT * FROM exp WHERE d_id=100;
```
![](imgs/20180408-205503.png)
###带IN关键字的查询
```
SELECT * FROM eml WHERE d_id IN(1000,1005);
//取值为1000或者1005的记录 NOT IN 同理
```
###带BETWEEN AND 或者NOT BETWEEN AND
###带LIKE的匹配查询
```
SELECT * FROM emp WHERE name LIKE 'SD';
//这里like等于=
SELECT * FROM emp WHERE name LIKE 'beijing%'
//beijing后边随便写，使用了通配符 like不等于=
SELECT * FROM exp WHERE name LIKE 'beijing_'
//beijing后边只能一个符
//一个汉字要两个_ _
```
###查询空值
```
SELECT * FROM work WHERE info IS (NOT) NULL;
```
###带AND的多条件查询（用来联合多个条件进行查询）
```
SELECT * FROM emp WHERE age<14 AND name='sd' AND id=2;
```
###带OR的多条件查询
```
SELECT * FROM emp WHERE age<14 OR name='sd' OR id=2;
```
###OR和AND可以同时用，但是AND运算优先
###查询结果不重复
```
SELECT DISTINCT d_id FROM emp;
```
### 对查询结果排序
```
SELECT * FROM emp ORDER BY age DESC,id ASC;
```
###分组查询
- 将查询结果按照某个字段或多个字段进行分组
- 一般和函数一起用GROUP BY，因为GROUP BY单独使用时只能查询分组的一条记录
```
SELECT * FROM sex,GROP_CONCAT(name) FROM employee GROUP BY sex;
SELECT sex ,COUNT(sex) FROM employee GROUP BY sex;
```
- 和HAVING一起用
```
SELEXT sex COUNT(sex) FROM emp GROUP BY sex HAVING COUNT(sex)>=3;
```
- 按多个字段进行分组
```
SELECT * FROM emp GROUP BY d_id ,sex;
//先按d_id,再按sex
```
- 和WITH ROLLUP 一起用，最后加上一条新纪录，计算总和
![](imgs/20180408-212518.png)
###用LIMIT限制查询结果的数量
- 不指定初始位置
```
SELECT * FROM emp LIMIT 2;
//只显示前两条
```
- 指定初始位置
```
SELECT * FROM emp LIMIT 0,2;
//第一个位置开始，显示两条
```
## 使用集合函数查询
```
SELECT COUNT(*) FROM emp;
SELECT d_id ,COUNT(*) FROM emp GROUP BY d_id;
SELECT num,SUM(score) FROM grade WHERE num=1001;
SELECT AVG(age) FROM emp;
SELECT AVG(score) FROM grade FROM grade GROUP BY course;
SELECT course,AVG(score) FROM grade GROUP BY course; 
SELECT MAX(age) FROM emp;
SELECT num,course,MAX(score) FROM grade GROUP BY course;
SELECT MIN(age) FROM emp;
```
##连接查询
###内连接查询
- 可以查询两个或两个以上的表，需要通过指定字段进行连接（要具有相同意义），当值相等就查出记录
```
SELECT num,name ,emp_id,d_nae FROM emp,dep WHERE emp_id=dep_id;
```
###外连接查询
- 两个或两个以上表，需要指定字段，字段相等时取记录，不等时也能查出来。外连接包括左连接和右连接
- 左连接：查出表1中的所有记录，表2的查询匹配的记录
```
SELECT num,name ,emp.d_id FROM emp LEFT JOIN dep ON emp.id = dep.d_id;
```
- 右连接：查出表2中的所有记录，表1的查询匹配记录
```
SELECT num,name ,emp.d_id FROM emp RIGHT JOIN dep ON emp.id = dep.d_id;
```
##子查询
- 内层查询的结果为外层查询语句提供查询条件
###带IN关键字的子查询
```
SELECT * FROM emp
			 WHERE d_id (NOT)IN
						(SELECT d_id FROM dep);						
```
###带比较运算符的子查询
```
SELECT id,name score FROM com_stu
							WHERE score>=
								(SELECT score FROM scholarship
								WHERE level=1);
```
###带EXISTS关键字的子查询
- 如果内层返回TRUE ，则执行外层，否则不执行
```
SELECT * FROM emp 
			WHERE EXISTS
					(SELECT d_name FROM dep
						WHERE d_id=1003);
```
- 条件表达式和EXITS关键字一起用
```
SELECT * FROM emp 
			WHERE age>20 AND EXISTS
					(SELECT d_name FROM dep
						WHERE d_id=1003);
```
###带ANY关键字的查询
```
SELECT * FROM stu WHERE score>=ANY (SELECT score FROM scholarship);
```
###带ALL关键字的子查询
```
SELECT * FROM stu WHERE score>=ALL (SELECT score FROM scholarship);
```
##合并查询结果
- UNION 和UNION ALL 的区别，前者去重后者没有
```
SELECT d_id FROM dep
UNION (ALL)
SELECT d_id FROM emp;
```
##为表和字段取别名
###表取别名
```
SELECT * FROM dep d WHERE d.d_id=1001;
```
###字段取别名
```
SELECT d_id AS dep_id,d_name AS dep_name FROM dep;
```
##使用正则表达式查询
![](imgs/20180408-222120.png)
```
'^aaa'  以aaa开头
's$' 以s结束
'^L..Y$' 两个.. 代替字符串中任意字符
'[cao]' 包含cao中任意一个字母
'[0-9]' 包含0-9任意
'[^a-z0-9]' 包含这些以外的字符
'ic'包含ic
'ic|uc|us' 或者的关系
'a+c' 中间至少一个字符
'a*c' 中间可以0个
'a{3}'出现过3次
'a{1,3}' 至少1次，之多3次
```
##问题
- 集合函数一般和GROUP BY用，除非如计算索引学生的平均分等
- 取别名主要可以简短和明确字段
- 使用通配符和正则表达式都可以模糊查询，不过正则更灵活
#第十一章：插入，查询与删除数据
