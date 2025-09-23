class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping={}
        lo=0
        mLen=-1

        for hi in range(len(fruits)):
            mapping[fruits[hi]]=mapping.get(fruits[hi],0)+1

            while(len(mapping)>2):
                mapping[fruits[lo]]-=1
                if(mapping[fruits[lo]]==0):
                    mapping.pop(fruits[lo])
                lo+=1
            
            if len(mapping)==2:
                mLen=max(mLen, hi-lo+1)  
                  
        if mLen==-1:
            for key in mapping:
                return mapping[key]
        else:
            return mLen
        
