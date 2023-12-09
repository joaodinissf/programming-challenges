def is_symbol(col):
    return col != "." and not col.isdigit() and col != "\n"


def has_symbol_adjacent(lines, ix_line, ix_col, ending_col):
    points_to_check = [
        (l, c)
        for l in [ix_line - 1, ix_line + 1]
        for c in range(ix_col - 1, ending_col + 2)
        if 0 <= l < len(lines) and 0 <= c < len(lines[l])
    ]
    points_to_check.extend(
        filter(
            lambda p: 0 <= p[1] < len(lines[0]), [(ix_line, ix_col - 1), (ix_line, ending_col + 1)]
        )
    )

    return any(is_symbol(lines[l][c]) for l, c in points_to_check)


def get_part_number_from_ix(lines, ix_line, ix_col):
    part_number = None

    if lines[ix_line][ix_col].isdigit():
        ending_col = ix_col
        while ending_col + 1 < len(lines[0]) and lines[ix_line][ending_col + 1].isdigit():
            ending_col += 1
        part_number = lines[ix_line][ix_col : ending_col + 1]

    return part_number


def get_part_numbers(lines):
    part_numbers = []

    ix_line = 0
    ix_col = 0
    while ix_line < len(lines) and ix_col < len(lines[ix_line]):
        if lines[ix_line][ix_col].isdigit():
            number_to_append = get_part_number_from_ix(lines, ix_line, ix_col)
            ending_col = ix_col + len(number_to_append) - 1
            if has_symbol_adjacent(lines, ix_line, ix_col, ending_col):
                part_numbers.append(int(number_to_append))
            ix_col = ending_col + 1
        else:
            ix_col += 1

        if ix_col >= len(lines[ix_line]):
            ix_col = 0
            ix_line += 1

    return part_numbers


def solve(input_file):
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]
    part_numbers = get_part_numbers(lines)
    return sum(part_numbers)


def main():
    test = True
    test = False

    if test:
        file_name = "d3/d3-p1-sample.txt"
    else:
        file_name = "d3/d3-p1.txt"

    expected_solution = 4361

    with open(file_name, "r") as f:
        solution = solve(f)
        print(solution)

        if test:
            assert solution == expected_solution


if __name__ == "__main__":
    main()
