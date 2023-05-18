def pascal_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(i-1):
               row.append(result[i-1][j] + result[i-1][j+1])
            row.append(1)
            result.append(row)
    for row in result:
        print(" " * (n-len(row)) + " ".join(str(x)for x in row))
    
pascal_triangle(8)



