def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of strings.
    """
    with open(filename, "r") as f:
        return f.readlines()



def main():
    # fall_2016_list = []
    for line in read_file("sample_grades.csv"):
        line = line.strip()
        line_list = line.split(",")
        print(line_list)



main()