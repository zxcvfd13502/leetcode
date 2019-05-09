class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:return[0]
        res=[0]
        for i in range(0,n):
            tmp=[]
            lr=len(res)
            for j in range(lr):
                tmp.append(res[lr-1-j]+2**i)
            res.extend(tmp)
        return res
                