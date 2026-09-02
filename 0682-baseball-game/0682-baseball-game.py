class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cs=0
        stack=[]
        for i in operations:
            if i =='+':
                a=stack[-2]+stack[-1]
                stack.append(a)
                cs+=a
            elif i=='C':
                cs-=stack.pop()
            elif i=='D':
                t=stack[-1]*2
                cs+=t
                stack.append(t)
            else:
                stack.append(int(i))
                cs+=int(i)
        return cs
        







        