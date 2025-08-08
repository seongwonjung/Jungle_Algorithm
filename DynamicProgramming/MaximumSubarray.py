# total_max(i) = max(total_max(i-1), cur_max(i))
# cur_max(i) = max(i_num + cur_max(i-1), i_num)

def maxSubArray(nums: List[int]) -> int:
    total_max = nums[0]
    cur_max = nums[0]
    
    for i in range(1, len(nums)):
        cur_max = max(nums[i] + cur_max, nums[i])
        total_max = max(total_max, cur_max)
        
    return total_max

# def maxSubArray(nums: List[int]) -> int:
#     total_max = [nums[0]]*len(nums)
#     cur_max = [nums[0]]*len(nums)
    
#     for i in range(1, len(nums)):
#         cur_max[i] = max(nums[i] + cur_max[i-1], nums[i])
#         total_max[i] = max(total_max[i-1], cur_max[i])
        
#     return total_max[len(nums)-1]