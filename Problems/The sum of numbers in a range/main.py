def range_sum(numbers, start, end):
    lst = [n for n in numbers if start <= n <= end]
    return sum(lst)


input_numbers = input().strip().split()
input_numbers = [int(n) for n in input_numbers]
a, b = input().strip().split()
print(range_sum(input_numbers, int(a), int(b)))
