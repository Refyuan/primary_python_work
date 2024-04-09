class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=1
        right=len(numbers)
        while left<right:
            res= numbers[left-1]+numbers[right-1]
            if res <target:
                left+=1
            elif res>target:
                right-=1
            else:
                return [left,right]