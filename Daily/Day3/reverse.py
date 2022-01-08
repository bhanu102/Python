#reverse the string
a = 'balayya'
rev = ''
for i in range(0,len(a)):
    rev = rev + a[len(a)-i-1]
print(rev)

#reverse the word n a string
a = 'Iam Learning Ubuntu'.split(' ')
new_lst = []
for i in a:
    new_lst.append(i[::-1])
print(' '.join(new_lst))