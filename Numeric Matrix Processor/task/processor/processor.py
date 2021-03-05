from math import floor


def menu():
    choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """)
    return choice


def check_type(num):
    if floor(float(num)) == float(num):
        return int
    else:
        return float


def data(r):
    arr1 = []
    for i in range(r):
        arr1.append(input().strip().split())
        t = check_type(arr1[0][0])
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


def matrix(mat, j):
    temp_mat = []
    for x in range(1, len(mat)):
        temp_mat.append([mat[x][y] for y in range(len(mat[x])) if y != j])
    return temp_mat


def matrix_2(mat, i, j):
    temp_mat = []
    for x in range(len(mat)):
        if x == i:
            continue
        temp_mat.append([mat[x][y] for y in range(len(mat[x])) if y != j])
    return temp_mat


def inverse(mat):
    det = determinant(mat)
    if not det:
        return 0
    minors = [[0 for i in range(len(mat))] for j in range(len(mat))]
    sign = 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            minors[i][j] = sign * determinant(matrix_2(mat, i, j))
            sign = -sign
    inverse_mat = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            inverse_mat[i][j] = minors[j][i] / det
    return inverse_mat


def determinant(mat):
    determinant.det = 0
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    sign = 1
    for i in range(len(mat[0])):
        determinant.det += sign * mat[0][i] * determinant(matrix(mat, i))
        sign = - sign
    return determinant.det


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
            t = check_type(const)
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
        elif choice == "5":
            m, n = input("Enter matrix size: ").strip().split()
            m, n = int(m), int(n)
            print("Enter matrix:")
            mat = data(m)
            print("The result is:\n{}".format(determinant(mat)))
        elif choice == "6":
            m, n = input("Enter matrix size: ").strip().split()
            m, n = int(m), int(n)
            print("Enter matrix:")
            mat = data(m)
            print("The result is:\n")
            inverse_mat = inverse(mat)
            if inverse_mat:
                for i in range(len(mat)):
                    print(*inverse_mat[i])
            else:
                print("This matrix doesn't have an inverse.")
        elif choice == "0":
            break


if __name__ == '__main__':
    main()
