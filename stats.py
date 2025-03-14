def get_num_of_words(text):
    words = text.split()                            #split text str into words
    word_count = len(words)                         #count number of words
    return word_count                               #return count

def get_num_of_chars(text):                         
    num_of_chars = {}                               #create chars dict
    for char in text:                               #loop over all chars in text string
        lowered = char.lower()                      #convert char into lower case
        if lowered in num_of_chars:                 #check if char already in num_of_chars dict
            num_of_chars[lowered] += 1              #add 1 to value of lowered char
        else:
            num_of_chars[lowered] = 1               #else create new key and set value to one
    return num_of_chars                             #return dictionary

def sort_on(dict):
    return dict["num"]

def sort_num_of_chars(num_of_chars):
    sorted_list = []
    for char in num_of_chars:
        sorted_list.append({"char": char, "num": num_of_chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list