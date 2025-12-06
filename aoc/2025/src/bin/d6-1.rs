use aoc_2025::read_input;

fn solve(input: &str) -> String {
    let mut total = 0;
    let mut problem_sets: Vec<Vec<u64>> = Vec::new();
    let mut operands: Vec<char> = Vec::new();

    for line in input.lines() {
        if line.chars().next().unwrap().is_numeric() {
            problem_sets.push(
                line.split_whitespace()
                    .map(|s| s.parse::<u64>().unwrap())
                    .collect(),
            );
        } else {
            operands = line
                .split_whitespace()
                .map(|s| s.chars().next().unwrap())
                .collect();
        }
    }

    for (ix, operand) in operands.iter().enumerate() {
        let problem_result = match operand {
            '+' => problem_sets.iter().map(|set| set[ix]).sum::<u64>(),
            '*' => problem_sets.iter().map(|set| set[ix]).product::<u64>(),
            _ => panic!("Unknown operand"),
        };
        total += problem_result;
    }
    total.to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
