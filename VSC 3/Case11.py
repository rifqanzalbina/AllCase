ukuran = int(input("Masukkan ukuran tabel = "))

# Mencetak baris atas 
print("+" + "-"*(ukuran-2) + "+")

# Mencetak bagian tengah
for i in range(ukuran-2):
    print("|" + " "*(ukuran-2)+"|")

# Mencetak bagian bawah
print("+" + "-"*(ukuran-2)+"+")