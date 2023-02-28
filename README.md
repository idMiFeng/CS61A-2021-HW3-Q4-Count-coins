# CS61A-2021-HW3-Q4-Count-coins
Use tree recursion to solve problems
![](https://img-blog.csdnimg.cn/img_convert/5846f55c76a9dfe8d716c7a8e2a87982.png)
![](https://img-blog.csdnimg.cn/img_convert/abe859ebe1ac15c80ef7c1be67d0743e.png)
Q4: Count coins
Given a positive integer change, a set of coins makes change for change if the sum of the values of the coins is change. Here we will use standard US Coin values: 1, 5, 10, 25. For example, the following sets make change for 15:

15 1-cent coins
10 1-cent, 1 5-cent coins
5 1-cent, 2 5-cent coins
5 1-cent, 1 10-cent coins
3 5-cent coins
1 5-cent, 1 10-cent coin
Thus, there are 6 ways to make change for 15. Write a recursive function count_coins that takes a positive integer change and returns the number of ways to make change for change using coins.
You can use either of the functions given to you:
ascending_coin will return the next larger coin denomination from the input, i.e. ascending_coin(5) is 10.
descending_coin will return the next smaller coin denomination from the input, i.e. descending_coin(5) is 1.
There are two main ways in which you can approach this problem. One way uses ascending_coin, and another uses descending_coin.
Important: Use recursion; the tests will fail if you use loops.
![](https://img-blog.csdnimg.cn/img_convert/ef71595019962b410aa3313b3aab46db.png)
![](https://img-blog.csdnimg.cn/img_convert/e9a1586072725133026c47820a2babfc.png)
What does count_partitions do in Partitions
![](https://img-blog.csdnimg.cn/img_convert/0e40f3030971621a09d28fd9fac3fa5f.png)
The function is to count the number of different implementation methods for dividing n into smaller numbers, and to stipulate that k is the largest number used for partitioning. For example, when k=3, only 1,2,3 numbers can be used for partitioning
To implement count_partitions(5,3), we first have to figure out how to partition. If we look at the partition method of 5 in the figure, methods 1 and 2 have 3 and the rest have none, so we can divide all the methods into two parts, one with at least one 3 and the rest with no 3. Then add up the numbers from the two parts to get the total method.
![](https://img-blog.csdnimg.cn/img_convert/709b4331da1e842f66edb64a976fe90b.jpeg)
Let's look at the first part, which is the methods that have at least one 3, because both methods 1 and 2 have at least one 3, so let's cancel that out, and then look at the rest, because 5 minus 3 is 2, and then the rest is dividing 2, and then dividing 2, So you implement count_partitions(2,3)
![](https://img-blog.csdnimg.cn/img_convert/299da3c56461b787c664e606f599021e.jpeg)
The second part can then be viewed as the return value of count_partitions(5,2), so we can say count_partitions(5,3)=count_partitions(2,3)+count_partitions(5,2), Then count_partitions(2,3) and count_partitions(5,2) we can do the same thing again, That's count_partitions(n,m)=count_partitions(n-m,m)+count_partitions(n,m-1) and that's the idea of tree recursion.
So what we're going to do with the return value, and what we're going to find is that we're not going to be able to see it directly or empirically, and we're going to have to debug a value, and then we're going to debug it to figure out what the function should return.
Using count_partitions(5,3) as an example, we found that when n&lt; At 0, there is no method, so return 0, when n=0, there is only one method, such as f(2,2)-&gt; f of 0,2, there's only one way 2 is equal to 2, so return 1. When m=, there is only one way, for example f(2,1) is 2=1+1, that is, return 1, then these three can be used as the end condition of the function call.
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8b1fa1267684a4886338ed2f9c3e5ad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)
Just change the m value of count_partitions(n,m) by a small amount. Take 15 for example, the partition number is 1,5,10,25. Because the title provides the function Descending_coin (25) =10. So it's easy to write the parsing

The result
![](https://img-blog.csdnimg.cn/img_convert/6807a24ee9478e2bb2721d6e0ec8fb56.png)