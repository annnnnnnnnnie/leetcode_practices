# 1 * 2 + 3 * 4 = ?
# expr = mult_expr '+'|'-' mult_expr
# mult_expr = digit ('*'|'/') digit |
import random


def parse_multiply_and_divide(line):
    MULT = '*'
    DIV = '/'
    for i in range(len(line)):
        token = line[i]
        if token == MULT or token == DIV:
            op1 = line[i - 1]
            op2 = line[i + 1]
            if token == MULT:
                result = int(op1) * int(op2)
            else:
                result = int(op1) / int(op2)
            line[i + 1] = result
            line[i] = ""
            line[i - 1] = ""
    return line


def parse_input(line):
    parse_multiply_and_divide(line)
    pass


"""
Lock A Lock B
Thread{ A.acquire(), B.acquire()}
Thread{ B.acquire(), A.acquire()}
"""


def main():
    songs_list = ['A', 'B', 'C', 'D']
    songs_priority = [60, 40, 3, 2]
    chosen_song = choose_song(songs_list, songs_priority)
    print("song chosen is", chosen_song)
    pass


def choose_song(songs_list, songs_priority):
    total = sum(songs_priority)
    choice = random.randint(0, total)
    current_sum = 0
    chosen_song = ""
    for i, p in enumerate(songs_priority):
        current_sum += p
        if choice < current_sum:
            chosen_song = songs_list[i]
            break
    return chosen_song


if __name__ == '__main__':
    for _ in range(10):
        main()
