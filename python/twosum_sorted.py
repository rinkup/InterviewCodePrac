# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(num, target):
    lnode, rnode = 0, len(num)-1
    while lnode < rnode:
        if target < (num[lnode] + num[rnode]):
            rnode -= 1
        elif target > (num[lnode] + num[rnode]):
            lnode += 1
        elif target == (num[lnode] + num[rnode]):
            return [lnode, rnode]
    return []
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))