class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split()
        last_element = ls[-1]
        l = len(last_element)
        return(l)