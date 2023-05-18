def extract_alphabets(input_string):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in input_string:
        if char in alphabets:
            result += char
    return result

string = "Hello Semuanya, Aku Rifqan Dan Aku Lagi beLajaR Pyhton TerimaKaSiH"
print("Alphabets:", extract_alphabets(string))