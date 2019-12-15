def two_sum(numbers, target):
    sum_counter = 0
    for i in numbers:
        if sum_counter == 0:
            sum_counter = sum_counter + 1
        elif sum_counter < target:
            sum_counter = sum_counter + 1
        elif sum_counter > target:
            sum_counter = i
        else:
            return sum_counter
