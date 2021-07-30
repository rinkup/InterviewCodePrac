# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(array, target):
    if len(array) > 1:
        for ele in array:
            remaining = target - ele
            if remaining in array:
                remaining_index = array.index(remaining)
                return [array.index(ele), remaining_index]
        return False
    else:
        return False
nums = [1, 2, 4, 6,  7, 8, 11, 15]
target = 9
print(two_sum(nums, target))
