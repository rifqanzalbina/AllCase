print ("=== KALKULATOR BMI ===")

# Meminta input dari User
berat_badan = float(input("Masukkan berat badan (dalam kilogram) : "))
tinggi_badan = float(input("Masukkan tinggi badan (dalam meter) : "))

# Menghitung BMI
bmi = berat_badan / (tinggi_badan ** 2)

# Menampilkan hasil
print("BMI anda adalah : ", bmi)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Underweight (Kurus)"
elif bmi >= 18.5 and bmi <= 24.9:
    kategori = "Normal (Ideal)"
elif bmi >= 25 and bmi <= 29.9:
    kategori = "Overweight Gemuk"
else:
    kategori = "Obesitas (Sangat Gemuk)"

print("Kategori BMI Anda adalah : " , kategori)