class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Early Return principle
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)# keyname	Required. The keyname of the item you want to return the value from value	Optional. A value to return if the specified key does not exist. Default value None
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True