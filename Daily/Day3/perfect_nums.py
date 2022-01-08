#print perfect nums for a given range
def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    return (True if sum == num and num !=1 and num != 0 else False)

n = int(input())
for x in range(n):
    if perfect_num(x):
        print(x)
# check perfect number or not 

n = int(input())
if perfect_num(n):
    print('Perfect Number')
else:
    print('Not a Perfect Number')