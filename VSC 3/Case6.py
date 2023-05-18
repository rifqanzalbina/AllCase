def nilai_maksimal_minimal(weight, wt, val, n):
    if n == 0 or weight == 0 :
        return 0
    if (wt[n-1] > weight):
        return nilai_maksimal_minimal(weight, wt, val,n-1)
    else:
        return max(val[n-1] + nilai_maksimal_minimal(weight-wt[n-1], wt, val, n-1), nilai_maksimal_minimal(weight, wt, val, n-1))

val = [60, 100, 120]
wt =[10, 20, 30, 40, 50]
weight = 330
n = len(val)

print(nilai_maksimal_minimal(weight, wt, val, n-1)) 