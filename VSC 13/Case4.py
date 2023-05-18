import numpy as np
a = np.random.rand(3,3)

print("Matriks acak: ")
print(a)

b = a * 5

print("\nMatriks setelah dikalikan dengan 5: ")
print(b)

det = np.linalg.det(a)
print(det)

inv = np.linalg.inv(a)
print(inv)

product = np.dot(a, inv)

print("\n Hasil perkalian matriks dengan inversnya")
print(product)


