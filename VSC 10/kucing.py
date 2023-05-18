class kucing:
    def __init__(self,nama,umur,warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def bersuara(self):
        print("Meow!")

    def tidur(self):
        print("Zzz..")

    def info(self):
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Umur : ", self.warna)

kucing1 = Kucing("Momo", 2 , "Putih")
kucing2 = Kucing("Kiki", 1, "Abu-Abu")



