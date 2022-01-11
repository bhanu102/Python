#ugly number or not
def ugly(num):
    if num == 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1
print(ugly(1))
print(ugly(100))
print(ugly(121))