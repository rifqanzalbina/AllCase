# Daftar tugas 

# Inisialisasi daftar tugas kosong 
to_do_list = []

# Fungsi untuk menambah tugas ke dalam daftar 
def add_task(task):
    to_do_list.append(task)
    print("Tugas", task, "Telah ditambahkan ke dalam daftar")

# Fungsi data yang disimpan dan akan dimunculkan 
def show_task():
    if len(to_do_list) == 0:
        print("Daftar Tugas Kosong.")
    else:
        print("Daftar Tugas")
        for task in to_do_list:
            print(task)

#   Fungsi untuk menghapus tugas dari daftar 
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print("Tugas", task, "Telah dihapus dari daftar.")
    else:
        print("Tugas", task, "Tidak ada dalam daftar.")

# Tampilan menu
print("Selamat datang di aplikasi pengelolaan daftar tugas (to-do-list)")

while True:
    print("\nPilih Kegiatan yang dilakukan : ")
    print("1. Tambah Tugas")
    print("2. Tampilkan daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    # Meminta input dari pengguna 
    pilihan = input("Masukkan Pilihan (1/2/3/4) : ")

    # Menjalankan Aksi yang Dipilih Oleh Pengguna 
    if pilihan == "1":
        task = input("Masukkan Tugas yang Ingin ditambahkan : ")
        add_task(task)
    elif pilihan == "2":
        show_task()
    elif pilihan == "3":
        task = input("Masukkan Tugas yang ingin dihapus : ")
        remove_task(task)
    elif pilihan == "4":
        print("Terima Kasih telah menggunakan aplikasi pengelolaan daftar Tugas.")
        break
    else:
        print("Input salah, Silahkan coba lagi.")
        