#check palindrome or not
def func(a):
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return False
        return True

a = 'malayalam'
# a = 'balayya'

if __name__ == '__main__':
    print(func(a))