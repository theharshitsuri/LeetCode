# 125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l1 = list(s)
        arr = []
        for i in l1:
            if i.isalnum():
                arr.append(i.lower())

        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True        