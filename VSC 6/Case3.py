# Program menghitung Luas dan keliling lingkaran 

# Impor Library math untuk menggunakan konstanta pi
import math

# Input dari user
jari_jari = float(input("Masukkan jari jari dalam cm : "))

# Menghitung luas lingkaran 
luas = math.pi * jari_jari

# Menghitung keliling lingkaran 
keliling = 2 * math.pi * jari_jari

# Menampilkan hasil 
print("Luas lingkaran adalah : ", luas, "cm^2")
print("Kelilling lingkaran adalah : ", keliling, "cm")