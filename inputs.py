def main():
    q1 = "What is your favorite movie?"
    fav_movie = input(q1)
    # print(fav_movie)
    q2 = f"What is your favorite character from {fav_movie}?"
    fav_char = input(q2)
    print(fav_char)
    q3 = f"What would you rate {fav_movie}?"
    rating = eval(input(q3))
    print(rating)
    print(eval("3+3"))
    print("3+3")
    print(eval("3" + "3"))


main()
