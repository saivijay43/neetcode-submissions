class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashmap(x):
            dict = {}
            for i in x:
                if i in dict.keys():
                    dict[i]+=1
                else:
                    dict[i]=1
            
            return dict
        return hashmap(s) == hashmap(t)

        