# print isomorphic or not for the given two strings
def func(str1,str2):
    #check length of the input strings are equal
    if len(str1)==len(str2):
        #initializing the empty dictionary
        d = {}
        #Iterating through str1 to map each character to str2
        for i in range(len(str1)):
            char1, char2 = str1[i], str2[i]
            # if char of str1 is in dictionary
            if char1 not in d:
                #if char of str2 is repeated in dictionary
                if char2 in d.values():
                    return False
                #mapping char1 in str1 to char2 in str2 (dictionary)
                d[char1] = char2
            #check the previous mapping values
            elif d[char1] != char2:
                return False
        return True
    return 'Length of the input strings are not equal.'
print(func('bhanu','bhanu'))
print(func('bhanu','gadupudi'))