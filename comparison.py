def main():

    list1 = [1, 2, 3]
    list2 = [-1, -2, -3]
    list3 = [-1, 2, -3]

    lists = [list1, list2, list3]
    sum_list = []
    for list in lists:
        sum_list.append(sum(list))
    print(sum_list, min(sum_list), max(sum_list))
    return
main()