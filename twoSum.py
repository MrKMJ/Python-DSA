class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}  # val -> index
        for index, element in enumerate(nums): 
            indices[element] = index
            #{
                # 4:0,
                # 5:1,
                # 6:2
            # }
        for index, element in enumerate(nums):
            diff = target - element
            if diff in indices and indices[diff] != index:
                return [index, indices[diff]]