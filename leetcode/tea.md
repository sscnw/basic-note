##实现 int sqrt(int x) 函数。
- 计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
 - 二分查找:以每一次的mid的平方来与target既数x相比：
如果mid*mid == x，返回mid；
如果mid*mid < x，那么说明mid过小，应让low = mid+1，在右边继续查找
如果mid*mid > x，那么说明mid过大，应让high = mid-1，在左边继续查找
若x无法开整数根号（在上述查找中没有找到），那么我们仍然可以利用之前对二分查找法总结的技巧，当target值不在数组中，low指向大于target的那个值，high指向小于target的那个值，由于我们需要向下取整的结果，所以我们返回high指向的值（这里high指向的值和high的值是同一个值），这个值就是所求得最接近起开根号结果的整数值。long来接溢出的值。
```
public int sqrt(int x) {
        int low = 0;
        int high = x;
        while(low<=high){
            long mid = (long)(low + high)/2;
            if(mid*mid < x)
                low = (int)mid + 1;
            else if(mid*mid > x)
                high = (int)mid - 1;
            else
                return (int)mid;
        }
        return high;
    }
```