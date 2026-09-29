class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [1]*n
        prefix = 1
        for i in range(n):
            lst[i] = lst[i]*prefix
            prefix = prefix*nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            
            lst[i] = lst[i]*suffix
            suffix = suffix*nums[i]
        
        return lst


        