# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(num, target):
    output = {} # val : index
    for index, value in enumerate(num):
        diff = target - value
        if diff in output:
            return [output[diff], index]
        output[value] = index
    return
num = [2, 2, 1, 5, 3]
target = 5
print(twoSum(num, target))