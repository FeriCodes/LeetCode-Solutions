class Solution(object):
    def isPalindrome(self, x):
        if x >= 0:
            new_x = str(x)
            if new_x[::-1] == new_x:
                return True
        return False
        