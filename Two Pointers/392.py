# 392. IS SUBSEQUENCE

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = 0
        for i in t:
            if p < len(s) and s[p] == i:
                p+=1
        return p == len(s)


        