class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s)) <= 1:
            return True
        
        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum():
                if l >= r:
                    break
                l+=1
            
            while not s[r].isalnum():
                if l >= r:
                    break
                r-=1

            if s[l] != s[r]:
                return False

            l+=1
            r-=1

        return True