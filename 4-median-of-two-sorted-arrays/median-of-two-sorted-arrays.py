class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            # Partition nums1
            i = (low + high) // 2

            # Partition nums2
            j = (m + n + 1) // 2 - i

            # Left and right values of nums1
            if i == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[i - 1]

            if i == m:
                right1 = float('inf')
            else:
                right1 = nums1[i]

            # Left and right values of nums2
            if j == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[j - 1]

            if j == n:
                right2 = float('inf')
            else:
                right2 = nums2[j]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # Move partition of nums1 to the left
            elif left1 > right2:
                high = i - 1

            # Move partition of nums1 to the right
            else:
                low = i + 1