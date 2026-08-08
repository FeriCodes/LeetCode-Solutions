class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = [] 
        index= 0
        for word in words:
            if x in word:
                result.append(index)
            index += 1
        return result