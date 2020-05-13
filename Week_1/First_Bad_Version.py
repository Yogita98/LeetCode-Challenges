# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n<2):
            return n
        low=1
        high=n
        while(low<=high):
            mid=int((low+high)/2)
            if(isBadVersion(mid)==True and isBadVersion(mid-1)==False):
                return mid
            elif(isBadVersion(mid-1)==True):
                high=mid-1
            else:
                low=mid+1