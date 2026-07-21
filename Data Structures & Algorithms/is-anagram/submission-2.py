class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) == 0 != len(t):
            return false
        
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        return s == t
        