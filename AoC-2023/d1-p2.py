def clean_line(line):
    spelled_out_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers = []
    for ix, c in enumerate(line):
        if c.isdigit():
            numbers.append(c)
        else:
            for word, digit in spelled_out_digits.items():
                if line[ix : ix + len(word)] == word:
                    numbers.append(digit)
                    break

    return numbers


def solve(input_file):
    lines = input_file.readlines()

    numbers = []
    for line in lines:
        numbers_in_line = clean_line(line)
        numbers.append(int(numbers_in_line[0] + numbers_in_line[-1]))

    return sum(numbers)


def main():
    file_name = "d1-p2-small.txt"
    file_name = "d1-p2.txt"
    with open(file_name, "r") as f:
        print(solve(f))


if __name__ == "__main__":
    main()
