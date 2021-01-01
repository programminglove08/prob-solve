#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMinIndex(nums):
                """
                :type nums: List[int]
                :rtype: int
                """
                n = len(nums) 
                if(nums[-1] >= nums[0]):
                    return 0

                lo, hi = 0, n -1 
                while lo <= hi:
                    mid = (lo+hi)//2
                    if (nums[mid] < nums[mid-1]): 
                        return mid
                    elif(nums[mid] > nums[mid+1]): 
                        return mid+1
                    else:              
                        if(nums[mid] > nums[0]):
                            lo = mid +1
                        else:
                            hi = mid - 1
       
        def binarySearch(nums, target, lo, hi):
            if lo <= hi:
                mid = (lo+hi)//2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] < target):
                    return binarySearch(nums, target, mid+1, hi)
                else:
                    return binarySearch(nums, target, lo, mid -1)
            return -1

        n = len(nums) 
        if(n == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
    
        min_index = findMinIndex(nums)
        if (nums[min_index] == target):
            return min_index
        if (min_index == 0):  
            return binarySearch(nums, target, 0, n-1)
        else:
            if(target < nums[0]): 
                return binarySearch(nums, target, min_index, n-1)
            else:
                return binarySearch(nums, target, 0, min_index-1)