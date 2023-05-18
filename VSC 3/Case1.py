# Check The Palindrome
def palindrome(word):
    return word == word[::-1]

# Input
word = input ("Input String = ")

# Check The Input
if palindrome(word):
    print(word,"adalah palindrome")
else:
    print(word,"adalah tidak palindrome")
