print("=== MENCARI NILAI MAKSIMUM DAN MINIMUM ===")

# Meminta input dari user
list_angka = input("Masukkan angka-angka yang dipisahkan dengan spasi : ")
list_angka = list(map(int, list_angka.split()))

# Mencari nilai maksimum dan minimum
nilai_max = max(list_angka)
nilai_min = min(list_angka)

# Menampilkan hasil
print("Nilai maksimum adalah : ", nilai_max)
print("Nilai minimum adalah : ", nilai_min)

