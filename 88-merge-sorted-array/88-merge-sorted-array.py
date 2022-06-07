class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        remove_element = len(nums1) - m
        # nums1.reverse()
        while remove_element:
            nums1.pop()
            remove_element = remove_element - 1
        # print(nums1)
        nums1.extend(nums2)
        # print(nums2)
        nums1.sort()
        