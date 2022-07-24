def all_splits(s):
    return [(s[:i], s[i:]) for i in range(len(s) + 1)]


def can_match(pattern: str, s: str) -> bool:
    if (not pattern) and (not s):
        return True
    elif pattern and (not s):
        p, ps = pattern[0], pattern[1:]
        return p == '*' and can_match(ps, s)
    elif (not pattern) and s:
        return False
    else:
        p, ps = pattern[0], pattern[1:]
        if p == '?':
            c, cs = s[0], s[1:]
            return c.isalnum() and can_match(ps, cs)
        elif p == '*':
            return any(
                [can_match(ps, tail) and all(map(lambda st: st.isalnum(), head))
                 for head, tail in all_splits(s)])
        else:
            c, cs = s[0], s[1:]
            return p.lower() == c.lower() and can_match(ps, cs)


def simplify_pattern(pattern: str) -> str:
    simplified = ""
    star_already_exists = False
    for c in pattern:
        if c == '*':
            if star_already_exists:
                continue
            else:
                simplified += c
                star_already_exists = True
        else:
            simplified += c
            star_already_exists = False
    return simplified


def main():
    pattern = input()
    s = input()
    simplified_pattern = simplify_pattern(pattern)
    result = can_match(simplified_pattern, s)
    if result:
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    main()
