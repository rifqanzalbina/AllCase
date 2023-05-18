print("=== PEMERIKSAAN BILANGAN PRIMA ===")

# Meminta input dari User
bilangan = int(input("Masukkan Bilangan : "))

# Memeriksa apakah bilangan prima atau tidak
if bilangan > 1:
    for i in range(2, bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "Bukan Bilangan Prima")
            break
    else:
        print(bilangan, "adalah bilangan primer")
else:
    print(bilangan, "Bukan Bilangan prima")