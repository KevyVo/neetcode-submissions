class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for letter in s:
            if letter in sMap:
                sMap[letter]+=1
            else:
                sMap[letter]=1
        
        for letter in t:
            if letter in tMap:
                tMap[letter]+=1
            else:
                tMap[letter]=1

        return sMap == tMap

        # Time = O(N) where N is the number of s+t 
        # Space = O(N) since the Hashmap is not nested so it also s+t