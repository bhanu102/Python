'''Given a string S consisting of uppercase and lowercase characters.
The task is to sort uppercase and lowercase letters separately
such that if the ith place in the original string
had an Uppercase character then it should not have a
lowercase character after being sorted and vice versa.'''
def func(a):
    l,u = [],[]
    for i in range(len(a)):
        if a[i].islower():
            l.append(a[i])
        elif a[i].isupper():
            u.append(a[i])
    lower,upper = sorted(l),sorted(u)
    res = ''
    x,y = 0,0
    for i in range(len(a)):
        if a[i].islower():
            res += lower[x]
            x += 1
        else:
            res += upper[y]
            y += 1
    return res
print(func('jdtAKJHkjjskjdSGYD'))