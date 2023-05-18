import kucing

kucing1 = Kucing("Momo", 2, "Putih")
kucing2 = Kucing("Kiki", 1, "Abu-abu")

# Memanggil metode pada objek Kucing
kucing1.bersuara()  # Output: Meow!
kucing2.tidur()     # Output: Zzzz...

# Mengakses atribut pada objek Kucing
print(kucing1.nama) # Output: Momo
print(kucing2.umur) 