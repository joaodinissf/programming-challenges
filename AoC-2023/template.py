def solve(input_file):
    lines = input_file.readlines()

    for line in lines:
        print(line)

    return 0


def main():
    with open("input.txt", "r") as f:
        print(solve(f))


if __name__ == "__main__":
    main()
