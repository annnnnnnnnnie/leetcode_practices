# bs = '(' bs ')'
#    | '[' bs ']'
#    | '{' bs '}'

# bs = ( '(' bs ')' | '[' bs ']' | '{' bs '}' ) {'(' bs ')' | '[' bs ']' | '{' bs '}'}
class PeekableIter:
    def __init__(self, content):
        self.content = list(content)
        self.current_index = 0
        self.max_index = len(self.content)

    def __next__(self):
        if self.current_index >= self.max_index:
            raise StopIteration
        else:
            item = self.content[self.current_index]
            self.current_index += 1
            return item

    def peek(self):
        if self.current_index >= self.max_index:
            raise StopIteration
        else:
            item = self.content[self.current_index]
            return item


class BasicBrackets:
    def __init__(self, inner_brackets):
        self.inner_brackets = inner_brackets
        self.left = ''
        self.right = ''

    def __str__(self):
        return self.left + str(self.inner_brackets) + self.right


class Braces(BasicBrackets):
    def __init__(self, inner_brackets):
        super().__init__(inner_brackets)
        self.left = '('
        self.right = ')'


class SquareBrackets(BasicBrackets):
    def __init__(self, inner_brackets):
        super().__init__(inner_brackets)
        self.left = '['
        self.right = ']'


class CurlyBrackets(BasicBrackets):
    def __init__(self, inner_brackets):
        super().__init__(inner_brackets)
        self.left = '{'
        self.right = '}'


def parse_brackets(tokens):
    brackets_list = []
    try:
        token = tokens.peek()
        if token == '(' or token == '[' or token == '{':
            token = next(tokens)
            if token == '(':
                inner_bs = parse_brackets(tokens)
                token = next(tokens)
                assert token == ')'
                brackets_list.append(Braces(inner_bs))
            elif token == '[':
                inner_bs = parse_brackets(tokens)
                token = next(tokens)
                assert token == ']'
                brackets_list.append(SquareBrackets(inner_bs))
            elif token == '{':
                inner_bs = parse_brackets(tokens)
                token = next(tokens)
                assert token == '}'
                brackets_list.append(CurlyBrackets(inner_bs))

            while True:
                try:
                    brackets = parse_brackets(tokens)
                    if brackets:
                        brackets_list.append(brackets)
                    else:
                        break
                except AssertionError:
                    raise RuntimeError("Cannot parse")
        else:
            return brackets_list
    except StopIteration:
        return brackets_list
    return brackets_list


def parser(tokens):
    try:
        result = parse_brackets(tokens)
        try:
            tokens.peek()
        except StopIteration:
            return True
        return False
    except RuntimeError:
        return False
    except Exception as e:
        raise e


def preprocess(input_string):
    return PeekableIter(filter(lambda c: bool(c), input_string))


def main():
    tokens = preprocess(input())
    result = parser(tokens)
    print(result)


if __name__ == '__main__':
    main()
