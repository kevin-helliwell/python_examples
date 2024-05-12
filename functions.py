def count_lines(filename):
    with open(filename) as file:
        line_count = 0
        for _ in file:
            line_count += 1
    return line_count


def count_words(filename):
    with open(filename) as file:
        word_count = 0
        for line in file:
            word_count += len(line.split())
    return word_count


def print_lines_words(filename):
    print(f"{count_lines(filename)} lines {count_words(filename)} words")
    return


def main():
    return


main()
