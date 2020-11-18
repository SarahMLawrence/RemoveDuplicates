Max_Chars = 256

def helper(s):
    string_count = [0] * Max_Chars
    for letter in s:
        string_count[ord(letter)] += 1
    return string_count
    

def first_not_repeating_character(s):
    new_count =  helper(s)
    index = -1
    n = 0
    
    for letter in s:
        if new_count[ord(letter)] == 1:
            index = letter
            break
        n += 1
        
    return index
    

    

