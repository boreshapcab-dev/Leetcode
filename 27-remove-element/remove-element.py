class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        common = []

        for digit in nums:
            if digit != val:
                common.append(digit)

        for i in range(len(common)):
            nums[i] = common[i]

        return len(common)