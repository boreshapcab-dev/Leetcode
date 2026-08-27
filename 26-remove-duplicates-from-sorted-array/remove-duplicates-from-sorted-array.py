class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        common = []

        for i in nums:
            if i not in common:
                common.append(i)

        for i in range(len(common)):
            nums[i] = common[i]

        return len(common)