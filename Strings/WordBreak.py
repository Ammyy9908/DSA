def word_break(string,word_list):
    if string in word_list:
        return True
    for i in range(1,len(string)):
        if string[:i] in word_list:
            if word_break(string[i:],word_list):
                return True
    return False


res = word_break("applepenapple",["apple","pen"])
