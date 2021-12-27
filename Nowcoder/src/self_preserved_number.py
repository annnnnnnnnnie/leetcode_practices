def generate_table(start, end):
    return [i for i in range(start, end) if is_self_preserved_num(i)]


def is_self_preserved_num(i):
    i_squared = i * i
    return str(i) == str(i_squared)[-len(str(i)):]


def execute_once():
    upper_bound = int(input())
    return


def main():
    while True:
        try:
            result = generate_table(1, 2000)
            print(len(result))
            print(*generate_table(1, 5))
        #             execute_once()
        except Exception:
            break


if __name__ == '__main__':
    main()
