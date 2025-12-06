use aoc_2025::read_input;

fn parse_input(input: &str) -> (Vec<String>, Vec<char>) {
    let mut problem_sets: Vec<String> = Vec::new();
    let mut operands: Vec<char> = Vec::new();

    for line in input.lines() {
        if line.chars().next().unwrap().is_numeric() {
            problem_sets.push(line.to_string());
        } else {
            operands = line
                .split_whitespace()
                .map(|s| s.chars().next().unwrap())
                .collect();
        }
    }
    return (problem_sets, operands);
}

fn get_next_number(
    problem_sets: &Vec<String>,
    problem_set_ix: usize,
) -> Result<u64, std::num::ParseIntError> {
    let mut number_str = String::new();

    for problem_set in problem_sets {
        number_str.push(problem_set.chars().nth(problem_set_ix).unwrap());
    }

    number_str.trim().parse::<u64>()
}

fn solve(input: &str) -> String {
    let (problem_sets, operands) = parse_input(input);
    let mut total = 0;

    let mut problem_set_ix = 0;
    for operand in operands {
        let mut problem_operands: Vec<u64> = Vec::new();
        while let Ok(next_operand) = get_next_number(&problem_sets, problem_set_ix) {
            problem_operands.push(next_operand);
            problem_set_ix += 1;
            if problem_set_ix >= problem_sets[0].len() {
                break;
            }
        }

        let partial_result = match operand {
            '+' => problem_operands.iter().sum::<u64>(),
            '*' => problem_operands.iter().product::<u64>(),
            _ => panic!("Unknown operand"),
        };
        total += partial_result;
        problem_set_ix += 1;

        // println!(
        //     "Operation: {} = {:?} => (Total: {})",
        //     problem_operands
        //         .iter()
        //         .map(|c| c.to_string())
        //         .collect::<Vec<String>>()
        //         .join(&format!(" {} ", operand)),
        //     partial_result,
        //     total
        // );
        // std::io::stdin().read_line(&mut String::new()).unwrap();

        if problem_set_ix >= problem_sets[0].len() {
            break;
        }
    }

    total.to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
