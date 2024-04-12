class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            if nums[left]+nums[right]>=target:
                right-=1
            else:
                ans+=1
                left+=1
        return ans
