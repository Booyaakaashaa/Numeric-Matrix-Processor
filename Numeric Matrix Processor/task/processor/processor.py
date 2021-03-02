from math import floor, pow


def menu():
    choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: """)
    return choice


def checktype(num):
    if floor(float(num)) == float(num):
        return int
    else:
        return float


def data(r):
    arr1 = []
    for i in range(r):
        arr1.append(input().strip().split())
        t = checktype(arr1[0][0])
        arr1[i] = [t(k) for k in arr1[i]]
    return arr1


def add(mat1, r1, c1, mat2, r2, c2):
    if (r1, c1) != (r2, c2):
        print(f"The operation cannot be performed.")
    print("The result is:")
    result = [[0] * c1] * r1
    for i in range(r1):
        for j in range(c1):
            result[i][j] = mat1[i][j] + mat2[i][j]
        print(*result[i])


def const_mul(mat, r, c, val):
    print("The result is:")
    for i in range(r):
        for j in range(c):
            mat[i][j] *= val
        print(*mat[i])


def mul(mat1, r1, c1, mat2, r2, c2):
    if c1 != r2:
        print(f"The operation cannot be performed.")
    result = []
    for i in range(r1):
        temp = []
        for j in range(c2):
            temp.append(0)
        result.append(temp)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j] += (mat1[i][k] * mat2[k][j])
        print(*result[i])


def transpose(mat, r, c, choice):
    if choice == "1":
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat[j][i])
            print(*temp)
    elif choice == "2":
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat[c - j - 1][r - i - 1])
            print(*temp)
    elif choice == "3":
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat[i][c - j - 1])
            print(*temp)
    else:
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat[r - 1 - i][j])
            print(*temp)


def determinant(mat, r, c, nr, nc):
    if r == c:
        if r == 1:
            return mat[0][0]
        if r == 2:
            return mat[nr][nc]
        for i in range(nr, c):
            if i != nc:
                return pow(-1, nr + i) * mat[nr][nc] * determinant(mat, r - 1, c - 1, nr + 1)




def main():
    while 1:
        choice = menu()
        if choice == "1":
            m1, n1 = input("Enter size of first matrix: ").strip().split()
            m1, n1 = int(m1), int(n1)
            print("Enter first matrix:")
            mat1 = data(m1)
            m2, n2 = input("Enter size of second matrix: ").strip().split()
            m2, n2 = int(m2), int(n2)
            print("Enter second matrix:")
            mat2 = data(m2)
            add(mat1, m1, n1, mat2, m2, n2)
        elif choice == "2":
            m, n = input("Enter size of matrix: ").strip().split()
            m, n = int(m), int(n)
            print("Enter matrix:")
            mat = data(m)
            const = input("Enter constant: ")
            t = checktype(const)
            const_mul(mat, m, n, t(const))
        elif choice == "3":
            m1, n1 = input("Enter size of first matrix: ").strip().split()
            m1, n1 = int(m1), int(n1)
            print("Enter first matrix:")
            mat1 = data(m1)
            m2, n2 = input("Enter size of second matrix: ").strip().split()
            m2, n2 = int(m2), int(n2)
            print("Enter second matrix:")
            mat2 = data(m2)
            mul(mat1, m1, n1, mat2, m2, n2)
        elif choice == "4":
            t_choice = input("""\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """)
            m, n = input("Enter size of matrix: ").strip().split()
            m, n = int(m), int(n)
            print("Enter matrix:")
            mat = []
            for i in range(m):
                mat.append(input().strip().split())
            transpose(mat, m, n, t_choice)
        elif choice == "0":
            break


if __name__ == '__main__':
    main()
