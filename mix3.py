def mix3(a: str, b: str, c: str) -> str:
    max_len = max(len(a), len(b), len(c))

    i = 0
    string = ""

    while i < max_len:
        if i < len(a):
            string += a[i]

        if i < len(b):
            string += b[i]

        if i < len(c):
            string += c[i]

        i += 1

    return string


def main():
    mix_value = mix3("Rust", "Python", "JavaScript")
    print(mix_value)


main()
