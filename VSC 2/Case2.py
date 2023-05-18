# Determining Leap Years Using Functions

# The Function
def years(year):
    leap = False
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
            if (year % 400 == 0 ):
                leap = True
    return leap

# Input That What You Want
year = int(input("Masukkan Tahun = "))

if years(year):
    print(year,"adalah tahun kabisat")
else:
    print(year,"bukan tahun kabisat")
