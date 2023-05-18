# Determining Leap Years Using Without Functions

# Input
year = int(input("Masukkan tahun = "))


# Logical Problem and Command Result
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print(year,"adalah tahun kabisat")
        else:
            print(year,"bukan tahun kabisat")
    else:
        print(year,"adalah tahun kabisat") 
else:
    print(year,"Bukan tahun kabisat")       