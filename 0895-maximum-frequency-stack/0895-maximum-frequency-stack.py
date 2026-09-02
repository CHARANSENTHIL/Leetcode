class FreqStack:

    def __init__(self):
        self.stack=[]
        self.hm={}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hm[val]=self.hm.get(val,0)+1

    def pop(self) -> int:
        max_freq = max(self.hm.values())
        for i in range(len(self.stack)-1,-1,-1):
            
            if self.hm[self.stack[i]] == max_freq:
                
                self.hm[self.stack[i]]-=1
                return self.stack.pop(i)




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()