# leetcode练习（初级）
## 1. 回文数字判断 

```
public static boolean isF(int x){
		int x1=x;
		boolean is=true;
		int res=0;
		if(x>0){
			while(x>0){
				res=x%10+res*10;
				x=x/10;
			}
			if(res!=x1){
				is=false;
			}
		}
		else if(x==0){
			is=true;
		}
		else
			is=false;
		return is; 
	}
```
### 测试用例：
- [ ] x=0
- [ ] 负数
- [ ] 正数
-----
##  2. 从排序数组中删除重复项（数组）
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。
示例：
```
给定数组: nums = [1,1,2],
你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
不需要理会新的数组长度后面的元素
```
```
class Solution {
    public int removeDuplicates(int[] nums) {
         // write your code here  
        if(nums.length == 0)  
        {  
            return 0;  
        }  
          
        int index = 1;  
        for(int i = 1; i < nums.length; i++)  
        {  
            if(nums[i] != nums[i-1])  
            {  
                nums[index++] = nums[i];  
            }  
        }  
          
        return index;  
    }
}
```
- 双指针

##3. 买卖股票的最佳时机 II（数组）
假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。
```
class Solution {
 public int maxProfit(int[] prices) {
        int result=0;
        if(prices.length==0){
            result=0;
        }
        for(int i=1;i<prices.length;i++){
            if(prices[i]>prices[i-1]){
                result=result+prices[i]-prices[i-1];
            }
        }
        return result;
    }
}

```
- 思路：假设下一天的价格比今天的高，就是有利润的，下一天的价格比今天的低，就应该抛售。
##4. 旋转数组（数组）
将包含 n 个元素的数组向右旋转 k 步。
例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

- 解法一：

```
class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;  
            while (k > 0)//循环几次就看k是多少  
            {  
                int t = 0;  
                t = nums[length - 1];//这是获取数组最高位置上的数字  
                for (int j = length - 2; j >= 0; j--)//从倒数第二个数字开始，倒叙循环。循环主要目的就是把其他数字位置都抬高一位  
                {  
                    nums[j + 1] = nums[j];  
                }  
                nums[0] = t;//抬高玩其他的，就可以直接把最高位上的数字赋值到0号位上了  
                k--;//完成一个循环  
            }  
    }
}
```
- 解法2
```

 public class Solution 
  {
      public void rotate(int[] nums, int k) 
      {
          if(nums == null || nums.length == 0 || k % nums.length == 0)
              return;
          
          int turns = k % nums.length;
          int middle = nums.length - turns;
         
         reverse(nums, 0, middle-1); // reverse left part
         reverse(nums, middle, nums.length-1); // reverse right part
         reverse(nums, 0, nums.length-1); // reverse whole part 
     }
     public void reverse(int[] arr, int s, int e)
     {
         while(s < e)
         {
             int temp = arr[s];
             arr[s] = arr[e];
             arr[e] = temp;
             
             s++;
             e--;
         }
     }
 }
```
- 解：举一个例子 

　　1 2 3 4 5 6 7　　如果k = 3 的话， 会变成 5 6 7 1 2 3 4

　　1 2 3 4 5 6 7　　middle = 7 - 3 = 4，分为左边 4个数字，右边 3个数字

　　4 3 2 1 7 6 5　　分别把左右reverse 一下

　　5 6 7 1 2 3 4　　把总数组reverse 一下就会得到答案
##存在重复（数组）
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。

- 解法1
```
class Solution {
 public boolean containsDuplicate(int[] nums) {
if (nums.length <= 1) {
            return false;
        }

        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(nums[i])) {
                return true;
            } else {
                hashMap.put(nums[i], i);
            }
        }
        
        return false;
    }
}
```
- 解法2
```
  public boolean containsDuplicate(int[] nums) {
       
        if (nums.length <= 1) {
            return false;
        }
        
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
}
```

##反转字符串
- 解法1  3ms
```
class Solution {
    public String reverseString(String s) {
     if(s == null)
        return null;
    int len = s.length();
    char[] cTmp = s.toCharArray();
    char[] cRes = new char[len];
    for (int i = 0; i < len; i++) {
        cRes[i] = cTmp[len-1-i];
    }
    String sRes = String.valueOf(cRes);
    return sRes;
    }
}
```
- 解法2 4ms
```
 public static String reverseString(String s) {

        StringBuilder stringBuilder = new StringBuilder(s.length());
        for (int i = s.length(); i > 0; i--) {
            stringBuilder.append(s.charAt(i-1));

        }
        String ss=stringBuilder.toString();
        return ss;
    }
```
- 解法3  2ms
```
 public String reverseString(String s) {
            if(s == null)
                return null;
            int len = s.length();
            char[] cTmp = s.toCharArray();
            char c;
            for (int i = 0; i < len>>1; i++) {
                c = cTmp[i];
                cTmp[i] = cTmp[len -1 - i];
                cTmp[len -1 - i] = c;
            }
            String sRes = String.valueOf(cTmp);
            return sRes;
        }
    
```
- 解法4 2ms
```
    public String reverseString(String s) {
    if(s == null || s.length() == 0)
            return "";
        char[] cs = s.toCharArray();
        int begin = 0, end = s.length() - 1;
        while(begin <= end){
            char c = cs[begin];
            cs[begin] = cs[end];
            cs[end] = c;
            begin++;
            end--;
        }
        return new String(cs);
	}
```
- 解法5 3ms
```
class Solution {
    public String reverseString(String s) {
   StringBuilder sb = new StringBuilder(s);
    return sb.reverse().toString();//reverse源码中也是用reverseString1（）这种方法，法234基本相同。StringBuilder线程不安全
	}
}

```

## 删除链表的结点
- 编写一个函数，在给定单链表一个结点(非尾结点)的情况下，删除该结点。

假设该链表为1 -> 2 -> 3 -> 4 并且给定你链表中第三个值为3的节点，在调用你的函数后，该链表应变为1 -> 2 -> 4。
```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
 public void deleteNode(ListNode node) {
    if(node==null||node.next==null) return;//如果p为空或为单链表中最后一个结点不符合题意，直接返回  
         ListNode q=node.next;//q为p的后继结点  
         node.val=q.val;
         node.next=q.next;//从单链表中删除结点q  
        }
        
     
}
```