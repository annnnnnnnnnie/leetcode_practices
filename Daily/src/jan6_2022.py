from functools import reduce


def simplify_path(path):
    paths = path.split('/')
    current_abs_path = ['']
    for p in paths:
        if not p or p == '.':
            continue
        elif p == '..':
            if len(current_abs_path) > 1:
                current_abs_path.pop()
        else:
            current_abs_path.append(p)
    if len(current_abs_path) == 1:
        return "/"
    else:
        return reduce(lambda p1, p2: p1 + '/' + p2, current_abs_path)


class Solution:
    def simplifyPath(self, path: str) -> str:
        return simplify_path(path)
