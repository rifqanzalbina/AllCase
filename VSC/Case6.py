angkaPertama = int(input("Masukkan Bilangan Pertama = "))
angkaKedua = int(input("Masukkan Bilangna Kedua = "))
angkaKetiga = int(input("Masukkan Bilangan Ketiga = "))

if (angkaPertama >= angkaKedua) and (angkaPertama >= angkaKetiga):
    largest = angkaPertama
elif (angkaKedua >= angkaPertama) and (angkaKedua >= angkaKetiga):
    largest = angkaKedua
else:
    largest = angkaKetiga

print("Bilangan Terbesar Adalah = ", largest)