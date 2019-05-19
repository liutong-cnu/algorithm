class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        save = set()
        res = ""
        for s in words:
            if(s[:-1] in save or s[:-1] == ""):
                if len(s) > len(res):
                    res = s
                save.add(s)
        
        return res
 
