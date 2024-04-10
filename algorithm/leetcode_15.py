from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-2):
            if nums[-3]+nums[-2]+nums[-1]<0:
                break
            x=nums[i]
            if i >0 and nums[i]==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2]>0:
                break
            j=i+1
            k=n-1
            while j<k:
                if x+nums[j]+nums[k]<0:
                    j+=1
                elif x+nums[j]+nums[k]>0:
                    k-=1
                else:
                    ans.append([x,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans