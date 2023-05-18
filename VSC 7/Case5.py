while True:
    print()
    print("Aplikasi Konversi Mata Uang")
    print("1. Konversi Mata Uang")
    print("2. Keluar")
    pilihan = input("Masukkan Pilihan Keberapa")

    # Panggil Fungsi yang sesuai berdasarkan pilihan pengguna
    if pilihan == "1":
        konversi_mata_uang()
    elif pilihan == "2":
        print("Terima Kasih telah menggunakan aplikasi konversi mata uang")
        break
    else:
        print("Pilihan yang dimasukkan tidak valid.")