class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s = s+f"{str(len(i))}#{i}"
        return s
        



    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j=j+1
            length = int(s[i:j])
            lst.append(s[j+1:j+1+length])
            i = j+1+length
        
        return lst

