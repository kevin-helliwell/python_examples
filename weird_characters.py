def main():
    weird_chars = []
    with open("austen.txt", "r") as file:
        for line in file:
            for character in line:
                if not character.isalnum():
                    weird_chars.append(character)
    print(set(weird_chars))
    return


main()
