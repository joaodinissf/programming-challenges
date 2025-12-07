use aoc_2025::read_input;
use std::iter::zip;
use std::thread;
use std::time::Duration;

fn clear_screen() {
    print!("\x1B[2J\x1B[1;1H");
}

fn pretty_print(row: &Vec<u64>) {
    clear_screen();
    println!();

    let symbols = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'];
    let num_levels = symbols.len() as u64;

    // Filter out zeros for calculating cutoffs
    let non_zero: Vec<u64> = row.iter().copied().filter(|&x| x > 0).collect();

    if non_zero.is_empty() {
        // All zeros
        for _ in row {
            print!(".");
        }
        println!();
        thread::sleep(Duration::from_millis(100));
        return;
    }

    let mut sorted_row = non_zero.clone();
    sorted_row.sort();
    let cut_offs: Vec<u64> = (1..num_levels)
        .map(|i| sorted_row[(sorted_row.len() * i as usize) / num_levels as usize])
        .collect();

    for &value in row {
        if value == 0 {
            print!(".");
        } else {
            let mut found = false;
            for (symbol, co) in zip(&symbols, &cut_offs) {
                if value <= *co {
                    print!("{}", symbol);
                    found = true;
                    break;
                }
            }
            if !found {
                print!("{}", symbols[symbols.len() - 1]);
            }
        }
    }
    println!();
    const FPS: u64 = 25;
    thread::sleep(Duration::from_millis(1000 / FPS));
}

fn solve(input: &str) -> u64 {
    let mut input_lines = input.lines();
    let mut current_row: Vec<u64> = input_lines
        .next()
        .unwrap()
        .chars()
        .map(|c| match c {
            '.' => 0,
            'S' => 1,
            _ => panic!("Unexpected character in input"),
        })
        .collect();

    let mut next_row = vec![0; current_row.len()];
    for line in input_lines {
        pretty_print(&current_row);
        for (i, c) in line.chars().enumerate() {
            if c == '^' {
                next_row[i - 1] += current_row[i];
                next_row[i + 1] += current_row[i];
            } else {
                next_row[i] += current_row[i];
            }
        }
        std::mem::swap(&mut current_row, &mut next_row);
        next_row.fill(0);
    }

    println!("{:?}", current_row);
    current_row.iter().sum()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
