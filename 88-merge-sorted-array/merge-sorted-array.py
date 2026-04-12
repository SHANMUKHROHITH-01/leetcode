class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for the end of actual elements in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # Set pointer for the very end of nums1 (the insertion point)
        p = m + n - 1
        
        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        # (If p1 remains, they are already in the correct place in nums1)
        nums1[:p2 + 1] = nums2[:p2 + 1]
        