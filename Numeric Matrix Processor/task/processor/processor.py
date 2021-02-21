m, n = input().strip().split()
m, n = int(m), int(n)
arr1 = []
for i in range(m):
    arr1.append(input().strip().split())
    arr1[i] = [int(k) for k in arr1[i]]
scalar = int(input())

add = [[0] * n] * m
for i in range(m):
    for j in range(n):
        add[i][j] = arr1[i][j] * scalar
    print(*add[i])
