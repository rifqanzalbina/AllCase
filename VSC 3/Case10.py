def kuadrat(angka):
    return angka**2
def kali_tiga(angka):
    return angka**3
def kali_empat(angka):
    return angka**4

list_angka = list(map(int, input("Masukkan angkanya = ").strip().split()))
hasil_kuadrat = map(kuadrat, list_angka)
hasil_kali_tiga = map(kali_tiga, list_angka)
hasil_kali_empat = map(kali_empat, list_angka)

list_hasil_kuadrat = list(hasil_kuadrat)
list_hasil_kali_tiga = list(hasil_kali_tiga)
list_hasil_kali_empat = list(hasil_kali_empat)

print("Hasil kuadrat = ", list_hasil_kuadrat)
print("Hasil Kali Tiga = ", list_hasil_kali_tiga)
print("Hasil Kali Empat = ", list_hasil_kali_empat)

