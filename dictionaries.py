def main():
    john_dict = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "country": "USA",
    }
    # name = john_dict["name"]
    # age = john_dict["age"]
    # city = john_dict["city"]
    # country = john_dict["country"]
    # print(name, age, city, country)

    for keys in john_dict.keys():
        print(keys)
    # for values in john_dict.values():
    #     print(values)
    # for key, value in john_dict.items():
    #     print(key, value)

    return


main()
