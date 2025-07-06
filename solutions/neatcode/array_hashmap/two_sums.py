from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []
        val_index_map = {}
        for i,n in enumerate(nums):
            val_index_map[n] = i

        for i ,n in enumerate(nums):
            diff = target - n

            if diff in val_index_map and val_index_map[diff] != i:
                output.append(i) # index
                output.append(map[diff]) # index
                return output

        return []




    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:

        output = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return output

