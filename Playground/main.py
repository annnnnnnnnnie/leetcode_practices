class A:
    def __init__(self):
        self.n = 1

    def get_number(self):
        return 1

    def get_n(self):
        return self.n


class B(A):
    def __init__(self):
        super().__init__()
        self.n = 2

    def get_number(self):
        return 2

    def get_n(self):
        return self.n


def main():
    b = B()
    a = A()
    a = b
    print("a.get number: ", a.get_number())
    print("b.get number: ", a.get_number())
    print("a.get n: ", a.get_n())
    print("b.get n: ", b.get_n())
    print("a.n: ", a.n)
    print("b.n: ", b.n)
    pass


if __name__ == '__main__':
    main()
