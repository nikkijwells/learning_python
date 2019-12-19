def two_sum(numbers, target):
    find_this = 0
    for i in numbers:
        find_this = target - i
        if find_this in numbers:
            #if numbers.index(find_this) == numbers.index(i):
                #find_this = "".join(numbers).Rfind(find_this)
                #Return (numbers.index(i), find_this)
            #else:
            return (numbers.index(i), numbers.index(find_this, (numbers.index(i) + 1)))


print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))
