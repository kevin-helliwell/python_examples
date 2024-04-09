def mix(a: str, b: str) -> str:
    return "".join([x + y for x, y in zip(a, b)]) + a[len(b) :] + b[len(a) :]


def main():
    print(mix("Rust", "Python"))


main()
