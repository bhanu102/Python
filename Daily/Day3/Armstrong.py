#print Armstrong number for a given range
def Armstrong_num(num):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return sum

n = int(input())
for x in range(1, n+1):
    if Armstrong_num(x) == x:
        print(x)
# Armstrong Number or Not
num = int(input())
if Armstrong_num(num) == num:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')