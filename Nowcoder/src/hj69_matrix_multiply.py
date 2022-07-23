def read_matrices(m, n, p):
    mat1 = [list(map(int, input().split())) for _ in range(m)]
    assert (len(mat1[0]) == n)
    mat2 = [list(map(int, input().split())) for _ in range(n)]
    assert (len(mat2[0]) == p)
    return mat1, mat2


def mat_multiply(m, n, p, mat1, mat2):
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            result[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(n)])
    return result


def print_mat(mat):
    for row in mat:
        print(*row)


def main():
    m = int(input())
    n = int(input())
    p = int(input())
    mat1, mat2 = read_matrices(m, n, p)
    result = mat_multiply(m, n, p, mat1, mat2)
    print_mat(result)


if __name__ == '__main__':
    main()
