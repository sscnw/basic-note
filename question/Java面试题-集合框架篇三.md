##1. ArrayList和Vector的区别
两个类都实现了List接口（List继承Collection接口），都是有序集合，有序，相当于动态数组，允许重复
- 同步性：Vector是线程安全的，它的方法之间时线程同步的，ArrayList相反。如果只有一个线程会访问到集合，那最好是ArrayList，效率高，否则Vector，这样就不用去考虑编写线程安全的代码
- 数据增长：ArrayList与Vector都有一个初始的容量大小，Vector默认增长为原来的两倍，ArraList增长为原来的1.5倍（源码中看到）。ArrayList与Vector都可以设置处死空间的大小，Vector还可以设置增长的空间大小，而ArrayList就没有提供设置增长空间的方法。
##2. HashMap和Hashtable的区别
- HashMap是Hashtable的轻量级实现。HashMap允许空的键值（key或value），线程非安全。
- HashMap把Hashtale的contains方法去掉了，改成了containskey，因为contains方法令人误解。
- Hashtable继承自Dictionary类，HashMap是Map的一个实现。
- Hashtable是Synchronize的，而HashMap不是
- 三方面
	- 历史原因：Hashtable是基于陈旧的Dictionary类的，HashMap是Map接口的一个实现
	- 同步性
	- 空值
##3. List和Map的区别
一个是存储单列数据的集合，另一个存储键值对。List有序，允许重复，Map无序，键不重复，值可以
##4. List ，Map，Set三个接口，存取元素的特点
- List与Set有相似性，都是单列元素的集合，所以，有同一个父接口Collection，Set不允许有重复元素，不能有两个相等对象（不仅仅是相同），add方法会返回一个boolean，可以加进去就是true。当集合含有与某个元素equals时，旧不能add。
- Set取元素，只能以iterator接口取得所有的元素，再逐一遍历。
- List表示有先后顺序的集合。插入值时，其实是在用这个集合的一个索引变量指向这个对象。当某个对象被add多次时，相当于集合中有多个索引指向了这个对象。List除了用iterator遍历，还可以用get（index i）说明取第几个
- Map与List和Set不同，双列。有put方法：put(obj key,obj value),每次存储时，要存储一对key/value，不能重复key，equals判断重复的，get(obj key).可以获得key集合，value集合，entry集合
- List特定次序持有元素，可重复元素。set无法拥有重复fauns，内部排序。Map保存键值对
##5. ArrayList ，Vector和LinkedList的存储特性
- ArrayList和Vector是以数组的方式存储数据，此数组元素数大于实际存储的数据以便增加和插入元素，都允许直接按序号索引元素，但是插入元素要设计数组元素移动的操作。LinkedList使用双向链表实现存储，按序号索引需要遍历，LinkedList也线程不安全。它中间提供了一些方法，使得它可以当作对战或者队列来使用
##6. 去掉Vector集合中一个重复的元素
```
Vector newVector = new Vector();
for(int i=0;i<vector.size();i++){
	Object obj=vector.get(i);
	if(!newVector.comtains(obj))
		newVector.add(obj);
}
```
```
HashSet set = new HashSet(vector);
```
## 7. Collection和Collections的区别
Collection是集合类的上级接口，继承他的接口主要有Set和List
Collections是针对集合类的一个帮助类，提供一系列静态方法实现对各种集合的搜索，排序，线程安全化等操作
##8. Set元素中如何区分重复
- equals方法
- ==用于比较两个基本数据类型和两个引用变量是否相等
- equals比较两个独立对象的内容
## 9. 集合类的主要方法
- 它们都有增删改查的方法
- set： add，remove，contains
- map：put，remove，contains
- List类有get（int index）方法
- map的get()参数是key，返回值是value