#sum of the digits in a string
a = 'bal1a2yya3'
sum = 0
for  i in a:
    if i.isdigit():
        sum = sum + int(i)
print(sum)