def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of strings.
    """
    with open(filename, "r") as f:
        return f.readlines()



def main():
    fall_grades = []
    spring_grades = []
    for line in read_file("sample_grades.csv"):
        line = line.strip()
        line_list = line.split(",")
        # print(line_list)
        if line_list[1] == "Spring 2016":
            spring_grades.append(line_list[2])
        if line_list[1] == "Fall 2016":
            fall_grades.append(line_list[2])
    print(spring_grades,fall_grades)



main()