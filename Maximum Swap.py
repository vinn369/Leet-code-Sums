class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(x) for x in str(num)]
        l_i={val:i for i, val in enumerate(nums)}
    
        for i in range(len(nums)):
            for d in range(9, nums[i],-1):
                if d in l_i and l_i[d]>i:
                    nums[i],nums[l_i[d]]=nums[l_i[d]],nums[i]
                    return int("".join(map(str,nums)))
        return num
