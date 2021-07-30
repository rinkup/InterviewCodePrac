def check_open_close(str):
    if str.count('{') != str.count('}'):
        return False
    elif str.count('[') != str.count(']'):
        return False
    elif str.count('(') != str.count(')'):
        return False
    else:
        return True
    
def is_valid(str):
    if(check_open_close(str)):
        open_para = []
        for alp in str:
            if alp == '{' or alp == '[' or alp == '(':
                open_para.append(alp)
            if alp == '}':
                if open_para.pop() != '{':
                    return False
            elif alp == ']':
                if open_para.pop() != '[':
                    return False
            elif alp == ')':
                if open_para.pop() != '(':
                    return False
        return True
    else:
        return False        
    
str = '(jh{j[][{([])}]}h)'
print(is_valid(str))
