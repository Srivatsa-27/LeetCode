class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num//2+1
        while left<=right:
            mid=(left+right)//2
            sqr=mid*mid
            if sqr==num: return True
            elif sqr<num:left=mid+1
            else:right=mid-1
        return False