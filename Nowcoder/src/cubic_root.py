EPSILON = 1e-9
NSF = 2


def main():
    x = float(input())
    cubic_root_x = compute_cubic_root(x)
    rounded_cubic_root = "{:.1f}".format(cubic_root_x)
    print(rounded_cubic_root)
    return


def compute_cubic_root(n):
    x0 = n
    f = f_(n)
    while not is_a_close_solution(n, x0):
        x0 = x0 - f(x0) / f_prime(x0)
    return x0


def f_(n):
    return lambda x: x ** 3 - n


def f_prime(x):
    return 3 * (x ** 2)


def is_a_close_solution(n, x0):
    return abs(f_(n)(x0)) < EPSILON


if __name__ == '__main__':
    main()
