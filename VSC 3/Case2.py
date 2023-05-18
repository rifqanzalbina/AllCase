# Check The Double Appearance

# Logical Problems
def multiple_appearance(num):
    frequency = {}
    for number in number:
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1
    result = []
    for number, count in frequency.items():
        if count == 2:
            result.append(number)
    return result

# Input and Print
numbers = list(map(int, input("Input the numbers without space = ").strip().split()))
print(multiple_appearance(numbers))

    

    