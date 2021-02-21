m, n = input().strip().split()
m, n = int(m), int(n)
arr1 = []
for i in range(m):
    arr1.append(input().strip().split())
    arr1[i] = [int(k) for k in arr1[i]]
x, y = input().strip().split()
x, y = int(x), int(y)
arr2 = []
for i in range(x):
    arr2.append(input().strip().split())
    arr2[i] = [int(k) for k in arr2[i]]
add = [[0] * n] * m
if m == x and n == y:
    for i in range(m):
        for j in range(n):
            add[i][j] = arr1[i][j] + arr2[i][j]
        print(*add[i])
else:
    print("ERROR")
