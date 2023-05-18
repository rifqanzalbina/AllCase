def total(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number 
    return sum

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Total:", total(numbers))