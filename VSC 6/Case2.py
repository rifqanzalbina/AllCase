# Program Menghitung Berat Badan Ideal

# Input

jenis_kelamin = input("Apakah anda Laki Laki atau perempuan? : ")
tinggi_badan = float(input("Berapa Tinggi Anda dalam cm? : "))

# Menghitung berat badan Ideal 

if jenis_kelamin.lower() == "laki_laki":
    berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)
else:
    berat_badan_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)

print("Berat Badan ideal anda yang harus dicapai adalah  : " , berat_badan_ideal, "Kg")