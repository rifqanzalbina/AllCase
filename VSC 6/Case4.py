# Fungsi penjumlahan 
def add(x, y):
    return x + y

# Fungsi pengurangan 
def substract(x,y):
    return x - y

# Fungsi perkalian
def multiply(x,y):
    return x * y

# Fungsi pembagian 
def divide(x,y):
    return x / y

# Tampilan menu 
print("Pilih Operasi.")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Menjalankan operasi yang dipilih oleh pengguna 
choice = input("Masukkan Pilihan (1/2/3/4) : ")

num1 = int(input("Masukkan Bilangan Pertama : "))
num2 = int(input("Masukkan Bilangan Kedua : "))

# Menjalankan operasi yang dipilih oleh pengguna 
if choice == "1":
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == "2":
    print(num1, "-", num2, "=", substract(num1,num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Input Salah")
