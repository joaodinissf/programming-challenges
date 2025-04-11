def solve(input_file):
    lines = input_file.readlines()

    sum = 0
    for line in lines:
        numbers_in_line = [x for x in line if x.isdigit()]

        number = int(numbers_in_line[0] + numbers_in_line[-1])

        sum += number

    return sum


def main():
    file_name = "d1-p1-small.txt"
    file_name = "d1-p1.txt"
    with open(file_name, "r") as f:
        print(solve(f))


if __name__ == "__main__":
    main()
