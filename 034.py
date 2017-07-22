class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #继续二分
        if len(nums)==0:return [-1,-1]
        start=0
        end=len(nums)-1
        flag=0
        while start<=end:
            if start==end:
                if (nums[start]==target):return [start,end]
                else:return [-1,-1]
            mid=(start+end)/2
            mids=mid
            while (nums[mid]==target):
                if mid>0 and flag==0:
                    if nums[mid-1]==target:mid-=1
                    else:
                        start=mid
                        flag=1
                        mid=mids
                elif mid==0 and flag==0:
                    start=0
                    flag=1
                    mid=mids
                elif mid<len(nums)-1 and flag==1:
                    if nums[mid+1]==target:mid+=1
                    else:
                        return [start,mid]
                else:return [start,mid]
            if nums[mid]<target:start=mid+1
            if nums[mid]>target:end=mid-1
        return [-1,-1]


