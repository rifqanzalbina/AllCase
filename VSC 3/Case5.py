def perpanjangan_yang_bertambah(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(perpanjangan_yang_bertambah([10,22,33,44,55,66,77,88]))