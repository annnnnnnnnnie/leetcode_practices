# If you need to import additional packages or classes, please import here.

def compute_sentence_avg_weight(words):
    n_words = len(words)
    total_weight = sum(map(len, words))
    return total_weight / n_words


def func():
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    words = input().strip().split()
    # please finish the function body here.
    sentence_avg_weight = compute_sentence_avg_weight(words)
    # please define the python3 output here. For example: print().
    print("{:.2f}".format(sentence_avg_weight))


if __name__ == "__main__":
    func()
