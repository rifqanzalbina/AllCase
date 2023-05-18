# Fungsi untuk mengkonversi suhu dari Celcius ke Fahrenheit
def celcius_ke_fahrenheit(suhu_celcius):
    suhu_fahrenheit = (suhu_celcius * 9/5) + 32
    return suhu_fahrenheit

# Fungsi untuk mengkonversi suhu dari Celcius ke Kelvin
def celcius_ke_kelvin(suhu_celcius):
    suhu_kelvin = suhu_celcius + 273.15
    return suhu_kelvin

# Meminta pengguna memasukkan suhu dalam derajat Celcius
suhu_celsius = float(input("Masukkan Suhu dalam derajat celcius : "))

# Menghitung suhu derajat Celcius ke Fahrenheit dan Kelvin
suhu_fahrenheit = celcius_ke_fahrenheit(suhu_celsius)
suhu_kelvin = celcius_ke_kelvin(suhu_celsius)

# Menampilkan hasil konversi Anda 
print(f"Suhu dalam derajat Fahrenheit : {suhu_fahrenheit:.2f}")
print(f"Suhu dalam derajat Kelvin : {suhu_kelvin:.2f}")