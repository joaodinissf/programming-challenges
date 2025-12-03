use aoc_2025::read_input;
use std::cmp::max;
fn solve(input: &str) -> String {
    let mut secret = 0;

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
        let current = max_1 * 10 + max_2;
        println!("{} --> {} {}", line, max_1, max_2);
        secret += current;
    }
    format!("{}", secret)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
