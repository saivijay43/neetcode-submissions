class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for i in nums:
            if i in hs:
                return True
                break
            else:
                hs.add(i)
        return False

        