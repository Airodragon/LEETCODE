class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        nums2.extend(nums3)
        nums3 = []
        nums1.extend(nums2)
        nums2 = []
        a = []
        d = Counter(nums1)
        nums1 = []
        for i in d:
            if d[i]>=2:
                a.append(i)
        return a