# No 1137

def tribonacci_table(n):
    table = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415,
             223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096,
             181997601, 334745777, 615693474, 1132436852, 2082876103]
    return table[n]


def tribonacci_iter(n):
    t_n = 0
    t_n_1 = 1
    t_n_2 = 1
    if n == 0:
        return t_n
    if n == 1:
        return t_n_1
    if n == 2:
        return t_n_2
    for _ in range(2, n):
        t_n_3 = t_n + t_n_1 + t_n_2
        t_n = t_n_1
        t_n_1 = t_n_2
        t_n_2 = t_n_3
    return t_n_3


class Solution:
    def tribonacci(self, n: int) -> int:
        return tribonacci_table(n)
