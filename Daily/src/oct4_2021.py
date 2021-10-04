def reformat_string(s: str):
    return s.replace('-', '').upper()


def separate_with(c, k, s):
    length = len(s)
    quotient = length // k
    remainder = length % k

    result = s[:remainder] + c if remainder else ""

    for i in range(quotient):
        result += s[remainder + k * i: remainder + k * (i + 1)]
        result += c
    return result[:-1]


def format_license_key(s, k):
    return separate_with('-', k, reformat_string(s))


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        return format_license_key(s, k)
