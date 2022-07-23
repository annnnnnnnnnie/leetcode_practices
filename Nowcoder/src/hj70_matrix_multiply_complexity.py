def read_mat_dimensions(n_mats):
    dimensions = []
    for _ in range(n_mats):
        m, n = map(int, input().split())
        dimensions.append((m, n))
    return dimensions


def parse_computation_sequence(com_seq: str):
    return None


def evaluate(ast, mat_dimensions):
    return 0


def main():
    n_mats = int(input())
    mat_dimensions = read_mat_dimensions(n_mats)
    computation_sequence = input()
    ast = parse_computation_sequence(computation_sequence)
    result = evaluate(ast, mat_dimensions)
    print(result)


if __name__ == '__main__':
    main()
