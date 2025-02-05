class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Compare length of list with length of set of list where set outputs the list with duplications removed.
        return len(nums) != len(set(nums))