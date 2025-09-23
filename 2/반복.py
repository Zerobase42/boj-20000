
def longest_repeated_substring(s):
    """
    문자열 s에서 가장 긴 반복 부분 문자열을 찾아 반환.
    없으면 빈 문자열 반환.
    """
    n = len(s)
    longest = ""
    # 모든 부분 문자열 탐색
    for i in range(n):
        for j in range(i+1, n):
            substr = s[i:j]
            if len(substr) > len(longest) and s.count(substr) > 1:
                longest = substr
    return longest


def smallest_repeating_unit(s: str) -> str:
    """
    문자열 s가 어떤 문자열을 반복해서 만들어졌다면,
    가장 작은 반복 단위를 찾아 반환.
    반복 패턴이 없으면 원래 문자열 반환.
    """
    n = len(s)
    for size in range(1, n//2+1):
        if n % size == 0:  # 길이가 나누어 떨어져야 반복 가능
            unit = s[:size]
            if unit * (n // size) == s:
                return unit
    return s


if __name__ == "__main__":
    s = open('prt.txt').read()

    print("문자열 길이:", len(s))

    # (1) 가장 긴 반복 부분 문자열
    lrs = longest_repeated_substring(s)
    print("가장 긴 반복 부분 문자열:", repr(lrs), " (길이:", len(lrs), ")")

    # (2) 전체를 구성하는 최소 반복 단위
    unit = smallest_repeating_unit(s)
    print("최소 반복 단위:", repr(unit), " (길이:", len(unit), ")")
