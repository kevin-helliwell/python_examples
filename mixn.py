def mixn(strings: list[str]) -> str:
    max_len = max(len(x) for x in strings)
    i = 0
    string = ""
    while i < max_len:
        for s in strings:
            if i < len(s):
                string += s[i]
        i += 1
    return string


def main():
    mix_value = mixn(
        [
            "Rust",
            "Python",
            "JavaScript",
            "C++",
            "Java",
            "OCaml",
            "Go",
            "C#",
            "Swift",
            "Kotlin",
        ]
    )
    print(mix_value)


main()
