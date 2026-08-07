class Solution(object):
    def lengthOfLastWord(self, s):
        result = s.split()
        return len(result[-1])
        
        