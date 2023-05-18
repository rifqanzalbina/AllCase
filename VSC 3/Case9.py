def kuadrat(x):
    return x**2


list_angka = [1, 2, 3, 4, 5]

hasil = map(kuadrat, list_angka)

list_hasil = list(hasil)

print(list_hasil)

