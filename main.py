# A subarray is a contiguous part of array,
# i.e. Subarray is an array that is inside another array

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# output: 6

def maxSubArray(self, nums: List[int]) -> int:
    max_sub_array = nums[0]  # assigning to the first value in the array
    current_sum = 0

    for n in nums:  # going through each number in nums
        if current_sum < 0:  # if at any point, current sum is negative, reset it to zero
            current_sum = 0
        current_sum += n  # add current number to current sum, to calc. the maximum number possible
        max_sub_array = max(max_sub_array, current_sum)  # compare max to itself to the sum just being computed
    return max_sub_array
