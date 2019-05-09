class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while(len(nums1)>m):
            nums1.pop()
        while(i<len(nums1) and j<n):
            if nums2[0]<nums1[i]:
                nums1.insert(i,nums2.pop(0))
                j=j+1
            i=i+1
        nums1.extend(nums2)
        