class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=1
        nonDupe=1

        for i in range(1, len(nums)):
            if(nums[nonDupe-1]!=nums[i]):
                nums[nonDupe]=nums[i]
                nonDupe+=1
        return nonDupe

