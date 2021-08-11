def letter_combinations(digits):
    num_dict = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    pre_digit = []
    
    for chr in digits:
        curr_digit = num_dict[int(chr)]
        if len(pre_digit) == 0:
            pre_digit = list(curr_digit)
        else:
            tmp = []
            for o in pre_digit:
                tmp += list(map(( lambda x: o + x), curr_digit))
            pre_digit = tmp
    return pre_digit


digit = '23456'
print(letter_combinations(digit))