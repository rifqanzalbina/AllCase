nilai = input("Masukkan Nilai Anda , pisahkan dengan spasi : ")

nilai_list = nilai.split()

jumlah = 0
for n in nilai_list:
    jumlah += int(n)

rata_rata = jumlah / len(nilai_list)

print("Nilai Rata-rata Anda Adalah : ", rata_rata)    