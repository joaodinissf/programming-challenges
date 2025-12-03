use aoc_2025::read_input;

fn solve_simpler(input: &str) -> String {
    let mut joltage = 0;

    for line in input.lines() {
        let chars: Vec<u32> = line.chars().map(|c| c.to_digit(10).unwrap()).collect();

        let max_1 = chars[..chars.len() - 1].iter().max().unwrap();
        let max_1_ix = chars.iter().position(|x| x == max_1).unwrap();

        let max_2 = chars[max_1_ix + 1..chars.len()].iter().max().unwrap();

        joltage += max_1 * 10 + max_2;
    }
    format!("{}", joltage)
}

fn solve(input: &str) -> String {
    let mut joltage = 0;

    for line in input.lines() {
        let chars: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();

        let mut max_1 = 0;
        let mut max_2 = 0;
        for (i, c) in chars.iter().enumerate() {
            if i == chars.len() - 2 {
                if *c > max_1 {
                    max_1 = *c;
                    max_2 = *chars.get(i + 1).unwrap();
                } else {
                    max_2 = *[max_2, *c, *chars.get(i + 1).unwrap()]
                        .iter()
                        .max()
                        .unwrap();
                }
                break;
            } else if *c > max_1 {
                max_1 = *c;
                max_2 = 0;
            } else if *c > max_2 {
                max_2 = *c;
            }
        }

        joltage += max_1 * 10 + max_2;
    }
    format!("{}", joltage)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);

    assert_eq!(result, solve_simpler(&contents));

    println!("{}", result);
    Ok(())
}
