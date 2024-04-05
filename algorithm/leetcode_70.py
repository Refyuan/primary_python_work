# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==1:
#             return 1
#         elif n==2:
#             return 2
#         else:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)
class Solution:
     def climbStairs(self, n: int) -> int:
         hashtable={}
         def climb(n:int):
             if n in hashtable:
                 return hashtable[n]
             if n==1:
                 return 1
             elif n==2:
                 return 2
             else:
                 hashtable[n]=climb(n-2)+climb(n-1)
                 return hashtable[n]
         return climb(n)
