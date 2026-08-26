# 67  6-$ forever
#Please RA AC avvu
#segtree should store Value and idx 
#we need max of max
class segtree_min:
    def __init__(self,n):
        self.tree=[[float('inf'),float('inf')] for _ in range(4*n)]
    def upd(self,l,r,node,idx,val,index):
        if l==r:
            if self.tree[node][0]>val:
                self.tree[node][0]=val
                self.tree[node][1]=index
            elif self.tree[node][0]==val:
                self.tree[node][1]=index
            return 
        mid=(l+r)>>1
        if idx<=mid:
            self.upd(l,mid,2*node+1,idx,val,index)
        else:
            self.upd(mid+1,r,node*2+2,idx,val,index)
        if self.tree[node*2+1][0]<self.tree[node*2+2][0]:
            self.tree[node]=self.tree[node*2+1]
        elif self.tree[node*2+1][0]>self.tree[node*2+2][0]:
            self.tree[node]=self.tree[node*2+2]
        else:
            if self.tree[node*2+1][1]>self.tree[node*2+2][1]:
                self.tree[node]=self.tree[node*2+2]
            else:
                self.tree[node]=self.tree[node*2+1]
    def query(self,l,r,node,ql,qr):
        if ql<=l and r<=qr:
            return self.tree[node]
        if qr<l or r<ql:
            return [float('inf'),float('inf')]
        mid=(l+r)>>1
        val1=self.query(l,mid,node*2+1,ql,qr)
        val2=self.query(mid+1,r,node*2+2,ql,qr)
        if val1[0]<val2[0]:
            return val1
        elif val1[0]>val2[0]:
            return val2
        else:
            if val1[1]>val2[1]:
                return val2
            else:
                return val1
class segtree_max:
    def __init__(self,n):
        self.tree=[[float('-inf'),float('-inf')] for _ in range(4*n)]
    def upd(self,l,r,node,idx,val,index):
        if l==r:
            if self.tree[node][0]<val:
                self.tree[node][0]=val
                self.tree[node][1]=index
            elif self.tree[node][0]==val:
                self.tree[node][1]=index
            return
        mid=(l+r)>>1
        if idx<=mid:
            self.upd(l,mid,2*node+1,idx,val,index)
        else:
            self.upd(mid+1,r,node*2+2,idx,val,index)
        if self.tree[node*2+1][0]<self.tree[node*2+2][0]:
            self.tree[node]=self.tree[node*2+2]
        elif self.tree[node*2+1][0]>self.tree[node*2+2][0]:
            self.tree[node]=self.tree[node*2+1]
        else:
            if self.tree[node*2+1][1]>self.tree[node*2+2][1]:
                self.tree[node]=self.tree[node*2+2]
            else:
                self.tree[node]=self.tree[node*2+1]
    def query(self,l,r,node,ql,qr):
        if ql<=l and r<=qr:
            return self.tree[node]
        if qr<l or r<ql:
            return [float('-inf'),float('-inf')]
        mid=(l+r)>>1
        val1=self.query(l,mid,node*2+1,ql,qr)
        val2=self.query(mid+1,r,node*2+2,ql,qr)
        if val1[0]<val2[0]:
            return val2
        elif val1[0]>val2[0]:
            return val1
        else:
            if val1[1]>val2[1]:
                return val2
            else:
                return val1
class Solution:
    def oddEvenJumps(self, nums: List[int]) -> int:
        """
        we can make a series of jumps 
        1st 3rd 5th 

        2nd 4th 6th 
        """
        """
        looks like stack propagation

        """
        """

        in first move odd number jumps 

        in second move even number jumps 

        in odd number jump we can move to the index j such that nums[i]<=nums[j] and nums[j] is smallest as possible and index j is small 
        as possible 



        in even number jump we go index most smallest possibel index j
        such that arr[i]>=arr[j] and arr[j] is largest as possible 


        in odd jump we need smallest of the largest greater than val-> 


        in even jump we need largest of the smallest less than a val-> 
        O(N) TC needed 


        How to precompute and find Those indexes use SegTree



        What is the MindMap Chako 
        --------------------------
        find the odd_jump_idx and even_jump_idx  

        ok Now we know odd_jump and even_jump idx 

        now how to find Good idx DSU ??  just dp -> as it is connectivity

        if it connects to end path   Reverse Iteration   



        DONtT GIVE up CHako


        Yes it is reverse Iteration 

        #SrujanDCForever


        #things i need val_map 

        #2 segment Trees No one is enough as both are Asking Min idx


        #any thing ELsee NO

        """
        n=len(nums)
        idx=0
        id_map=defaultdict(int)
        for val in sorted(nums):
            if val not in id_map:
                id_map[val]=idx
                idx+=1
        #anyways index 1 update is not required
        dp_even=[0]*(n)
        dp_odd=[0]*(n)
        #dp_even[i] -> 0 not possible 1->possible 
        #dp_odd[i] -> 0 not possible 1->possible
        dp_even[-1]=1
        dp_odd[-1]=1
        #as they are all ready at the end
        st_odd=segtree_min(idx)
        st_even=segtree_max(idx)
        st_even.upd(0,idx-1,0,id_map[nums[-1]],nums[n-1],n-1)
        st_odd.upd(0,idx-1,0,id_map[nums[-1]],nums[n-1],n-1)
        for i in range(n-2,-1,-1):
            #the odd jump id is greater than or equal to the val
            val1,odd_jump_id=st_odd.query(0,idx-1,0,id_map[nums[i]],idx-1)
            val2,even_jump_id=st_even.query(0,idx-1,0,0,id_map[nums[i]])
            # print(f"jumped to {val1},{odd_jump_id} when odd jump at {i}")
            # print(f"jumped to {val2},{even_jump_id} when even jump at {i}")
            if even_jump_id!=float('-inf'):
                if dp_odd[even_jump_id]:
                    dp_even[i]=1
            if odd_jump_id!=float('inf'):
                if dp_even[odd_jump_id]:
                    dp_odd[i]=1
            st_odd.upd(0,idx-1,0,id_map[nums[i]],nums[i],i)
            st_even.upd(0,idx-1,0,id_map[nums[i]],nums[i],i)
        cnt=0
        for i in range(n):
            if dp_odd[i]:
                print(i)
                cnt+=1
        return cnt