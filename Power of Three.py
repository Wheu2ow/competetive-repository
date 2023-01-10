class Solution(object):
    def isPowerOfThree(self, n):
        if n==0:
            return False
        if n%3==0:
            return True
