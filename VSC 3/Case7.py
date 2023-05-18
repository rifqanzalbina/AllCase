def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

angka = int(input("Input the number = "))
hasil = faktorial(angka)
print("factorial of", angka, "is" , hasil)

