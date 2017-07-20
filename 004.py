class Solution(object):


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lA=len(nums1)
        lB=len(nums2)
        if (lA+lB)%2==1:
            return self.getKth(nums1,nums2,(lA+lB)/2+1)
        else:
            return (self.getKth(nums1,nums2,(lA+lB)/2)+self.getKth(nums1,nums2,(lA+lB)/2+1))*0.5




    def getKth(self, A, B, k):  # 实现一个寻找第k大的数（递归）
        lA = len(A)
        lB = len(B)
        if lB > lA: return self.getKth(B, A, k)  # 将小的array置于前
        if lA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k / 2, lA)  # 二分查找
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:  # 当A[pa-1]较时 意味着第k个数比A[pa-1]大 所以在剩下的数中搜索k-pa大的数
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)







