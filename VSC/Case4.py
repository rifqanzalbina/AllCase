def extract_odd_numbers(input_list):
    result = []
    for number in input_list:
        if number % 2 != 0:
            result.append(number)
    return result

numbers = list(map(int, input("Masukkan angka-angkanya = ").split()))
print("Extract Numbers: ", extract_odd_numbers(numbers))
