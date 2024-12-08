# x - wrong character
# ? - right character, wrong spot
# ! - right character, right spot

def check_guess(guess, correct_word):
    for index, value in enumerate(guess):
        if value == correct_word[index]:
            print(value, "is in the correct spot")
        else:
            print(value, "is not in the correct spot")

    return

def main():
    word = "vivid"
    return