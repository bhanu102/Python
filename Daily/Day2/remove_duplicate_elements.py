#removing duplicate elements in a string
a = 'bhanuuu'
result = ''
for ch in a:
    if ch not in result:
        result += ch
print(result)
    
#using the list and join
a = 'bhanuuu'
l = []
[l.append(ch) for ch in a if ch not in l]
result = ''.join(l)
print(result)

#using the set and join
a = 'bhanuu'
b = set(a)
print(''.join(b))