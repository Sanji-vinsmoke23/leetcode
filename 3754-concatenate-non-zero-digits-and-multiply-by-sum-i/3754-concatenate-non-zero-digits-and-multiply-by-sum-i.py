class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum=0

        for i in str(n):
            num=int(i)
            if num != 0:
                x=x*10+num
                sum+=num
        return x*sum