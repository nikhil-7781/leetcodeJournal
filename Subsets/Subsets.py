class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        sub=[]
        def dfs(i):
            if i>=len(nums):
                res.append(sub.copy())
                return #exit that particular recursive call
            #include nums[i]
            sub.append(nums[i])
            dfs(i+1)

            #exclude nums[i]
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res

