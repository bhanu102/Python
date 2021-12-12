# num=[1,2,3,4,5]
# i_nums=iter(num)

# # print(next(i_nums))
# # print(next(i_nums))

# for i in i_nums:
#     print(i)

class Range:

    def __init__(self, start, end):
        self.val = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.val >= self.end:
            raise StopIteration
        current = self.val
        self.val += 1
        return current

nums=Range(1,10)

print(next(nums))

for i in nums:
    print(i)
