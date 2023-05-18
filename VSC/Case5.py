def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Masukkan sebuah string: ")
vowel_count = count_vowels(input_string)
print("Jumlah huruf vokal dalam string:", vowel_count)