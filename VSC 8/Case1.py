print("=== Konversi Bilangan ===")

# Meminta input dari user
bilangan = int(input("Masukkan Bilangan Desimal : "))

# Mengkonversi bilangan ke biner, oktal, dan heksadesimal
biner = bin(bilangan)
oktal = oct(bilangan)
heksa = hex(bilangan)

# Menampilkan hasil
print("Bilangan Desimal", bilangan, "Dalam Bentuk : ")
print("Biner", biner)
print("Oktal", oktal)
print("Hexadesimal", heksa)

