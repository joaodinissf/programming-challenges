use aoc_2025::read_input;

fn solve(input: &str) -> u32 {
    let mut input_lines = input.lines();
    let mut current_line = input_lines.next().unwrap().replace("S", "|");
    let mut num_splits = 0;

    for line in input_lines {
        for (i, c) in line.chars().enumerate() {
            if c == '^' && current_line.chars().nth(i) == Some('|') {
                // No need to check bounds here since we know no splitters are at the edges
                current_line.replace_range(i - 1..=i + 1, "|.|");
                num_splits += 1;
            }
        }
    }

    num_splits
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
