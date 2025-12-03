use aoc_2025::read_input;

const MAX_CHARS: usize = 12;

fn get_line_max_joltage(line: &str) -> u64 {
    let mut last_ix: usize = 0;
    let mut joltage: String = String::with_capacity(MAX_CHARS);

    let line_digits: Vec<u32> = line.chars().map(|c| c.to_digit(10).unwrap()).collect();

    for remaining_chars in (1..=MAX_CHARS).rev() {
        let slice = &line_digits[last_ix..(line_digits.len() - remaining_chars + 1)];
        let max_in_slice = slice.iter().max().unwrap();
        let max_in_slice_ix = slice.iter().position(|&x| x == *max_in_slice).unwrap();

        joltage.push_str(&max_in_slice.to_string());

        last_ix += max_in_slice_ix + 1;
    }

    joltage.parse().unwrap()
}

fn solve(input: &str) -> String {
    let mut secret: u64 = 0;
    for line in input.lines() {
        secret += get_line_max_joltage(line);
    }
    format!("{}", secret)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
