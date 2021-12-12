def squares(list):
    for i in list:
        yield(i*i)

result=squares([1,2,3,4,5])
for num in result:
    print(num)