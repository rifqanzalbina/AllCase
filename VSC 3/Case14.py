def permutation(data, i ,length):
    if i == length:
        print(" ".join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

def print_permutation(string):
    permutation(list(string ), 0, len(string))

print_permutation("abcdefgh")