class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def dicts(nums):
            dict = {}
            for i in nums:
                if i in dict.keys():
                    dict[i]+=1
                else:
                    dict[i]=1
            return dict
        dict = dicts(nums)
        sorted_dict = sorted(dict.items(), key=lambda item: item[1],reverse=True)
        lst = []
        for i in range(k):
                lst.append(sorted_dict[i][0])
        return lst