# Meminta pengguna memasukkan teks dan kata yang ingin dicari
teks = input("Masukkan Sebuah Teks : ")
kata = input("Masukkan Sebuah kata yang ingin dicari : ")

# Menghitung kemunculan kata dalam teks 
jumlah_kemunculan = teks.count(kata)

# Menampilkan 
print(f"Jumlah Kemunculan kata '{kata}' dalam setiap teks adalah {jumlah_kemunculan}.")