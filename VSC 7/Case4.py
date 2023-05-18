tanggal_penting = {
    '20 Januari' : 'Hari Kesadaran Nasional',
    '14 Februari' : 'Hari Valentine',
    '21 Maret' : 'Hari Kebun Raya Indonesia',
    '22 Maret' : 'Hari Air Sedunia',
    '22 April' : 'Hari Bumi',
    '1 Mei' : 'Hari Buruh Internasional',
    '20 Mei' : 'Hari Kebangkitan Nasional',
    '1 Juni' : 'Hari Lahir Pancasila',
    '5 Juni' : 'Hari Lingkungan Hidup Sedunia',
    '17 Agustus' : 'Hari Kemerdekaan Indonesia',
    '18 November' : 'Hari Pahlawan',
    '25 Desember' : 'Natal',
    '30 Juli' : 'Ulang tahun',
}

# Def untuk Menambahkan Tanggal Penting
def tambah_tanggal_penting():
    tanggal = input("Masukkan Tanggal (DD MM) : ")
    deskripsi = input("Masukkan Deskripsi : ")
    tanggal_penting[tanggal] = deskripsi
    print("Tanggal Berhasi Ditambahkan")

# Def Untuk Menampilkan Tanggal
def tampilkan_tanggal_penting():
    print("Berikut adalah tanggal penting yang tersimpan")
    for tanggal, deskripsi in tanggal_penting.items():
        print(tanggal, "-", deskripsi)

# Mencari Tanggal Penting
def cari_tanggal_penting():
    kata_kunci = input("Masukkan kata kunci : ")
    ditemukan = False
    for tanggal, deskripsi in tanggal_penting.items():
        if kata_kunci.lower() in deskripsi.lower():
            print(tanggal, "-",deskripsi)
            ditemukan = True
    if not ditemukan:
        print("Tanggal penting tidak ditemukan")

# Prosesnya
while True:
    print()
    print("Aplikasi pengingat tanggal")
    print("1. Tampilkan semua tanggal penting")
    print("2. Tambahkan tanggal penting baru")
    print("3. Cari tanggal penting")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3/4) : ")

    if pilihan == "1":
        tampilkan_tanggal_penting()
    elif pilihan == "2":
        tambah_tanggal_penting()
    elif pilihan == "3":
        cari_tanggal_penting()
    elif pilihan == "4":
        print("Terima Kasih Telah menggunakan Aplikasi pengingat tanggal ini :D")
        break
    else:
        print("Pilihan yang dimasukkan tidak valid.")






