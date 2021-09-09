# Write a function diff(arrA, arrB) that accepts two arrays and returns a new array that contains all values that are not contained in both input arrays. The order of numbers in the result array does not matter.

# Examples
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# diff(a, b) # => [1, 2, 5, 6]
# Note: we don't care if numbers are out of order or repeated; for example, these two arrays are equivalent since they are re-arrangements of the same values:

# a = [1, 2, 1]
# b = [2, 1, 2]

# diff(a, b) # => []

def diff(a, b):
    return list(set(a)^set(b))
    # return list(set(a) - set(b)) + list(set(b) - set(a))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(diff(a, b))