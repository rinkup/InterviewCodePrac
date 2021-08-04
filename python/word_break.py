def validWord(s, dict):
    for word in wordDict:
        if word in s:
            s = s.replace(word, '')
    if len(s) > 0:
        return False
    else:
        return True


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(validWord(s, wordDict))