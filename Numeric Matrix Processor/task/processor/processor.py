from math import floor
def menu():
    choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
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
    result = [[0] * c2] * r1
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j] += (mat1[i][k] * mat2[k][j])
        print(*result[i])


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
        elif choice == "0":
            break


if __name__ == '__main__':
    main()
