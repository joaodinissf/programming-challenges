def solve(input_file):
    lines = input_file.readlines()

    for line in lines:
        print(line)

    return 0


def main():
    test = True
    # test = False

    if test:
        file_name = "d3/d3-p1-sample.txt"
    else:
        file_name = "d3/d3-p1.txt"

    expected_solution = 0

    with open(file_name, "r") as f:
        solution = solve(f)
        print(solution)

        if test:
            assert solution == expected_solution


if __name__ == "__main__":
    main()
