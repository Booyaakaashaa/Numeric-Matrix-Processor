def last_indexof_max(numbers):
    ind = -1
    top = -100000
    for i in range(len(numbers)):
        if numbers[i] >= top:
            top = numbers[i]
            ind = i
    return ind

    # write the modified algorithm here
