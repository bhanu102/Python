#check rotation of each other or not
def func(str1,str2):
    str1,str2 = str1.lower(),str2.lower()
    if sorted(set(str1)) == sorted(set(str2)):
        res = str1+str2
        countstr2 = res.count(str2)
        if countstr2 > 0:
            print("Rotations of each other")
    
    else:
      print("Not rotations of each other")
func('hello','bhanu')
func('hello','elloh')
func('hello','llohe')
func('bhanu','gadupudi')

#left rotation and right rotation