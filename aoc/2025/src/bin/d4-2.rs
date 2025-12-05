use aoc_2025::read_input;
use std::thread::sleep;

fn is_accessible(grid: &Vec<Vec<char>>, row_ix: i32, col_ix: i32) -> bool {
    if grid[row_ix as usize][col_ix as usize] != '@' {
        return false;
    }

    let mut neighbor_rolls = 0;
    for i in -1..=1 {
        for j in -1..=1 {
            if i == 0 && j == 0 {
                continue;
            }

            let r = row_ix + i;
            let c = col_ix + j;

            if r >= 0 && r < grid.len() as i32 && c >= 0 && c < grid[0].len() as i32 {
                if grid[r as usize][c as usize] == '@' {
                    neighbor_rolls += 1;
                    if neighbor_rolls >= 4 {
                        return false;
                    }
                }
            }
        }
    }
    true
}

fn remove_rolls_pretty(grid: &Vec<Vec<char>>) -> u32 {
    let mut removed_roll_count = 0;
    let mut removed_roll = true;
    let mut grid = grid.clone();

    println!("\x1B[2J\x1B[1;1H");
    println!("Iterating...");
    for row in grid.iter() {
        let line: String = row.iter().collect();
        println!("{}", line);
    }

    let mut iteration = 0;
    while removed_roll {
        removed_roll = false;
        let mut removable_positions: Vec<(i32, i32)> = Vec::new();
        for row_ix in 0..grid.len() as i32 {
            for col_ix in 0..grid[row_ix as usize].len() as i32 {
                if is_accessible(&grid, row_ix, col_ix) {
                    removable_positions.push((row_ix, col_ix));
                    removed_roll_count += 1;
                    removed_roll = true;
                }
            }
        }

        for (row_ix, col_ix) in removable_positions {
            grid[row_ix as usize][col_ix as usize] = '.';
        }

        println!("\x1B[2J\x1B[1;1H");
        println!("Iteration {}", iteration);
        for row in grid.iter() {
            let line: String = row.iter().collect();
            println!("{}", line);
        }
        // std::io::stdin().read_line(&mut String::new()).unwrap();
        const FPS: u32 = 15;
        sleep(std::time::Duration::from_millis(1000 / FPS as u64));
        iteration += 1;
    }

    removed_roll_count
}

fn remove_rolls_simple(grid: &Vec<Vec<char>>) -> u32 {
    let mut removed_roll_count = 0;
    let mut removed_roll = true;
    let mut grid = grid.clone();

    while removed_roll {
        removed_roll = false;
        let mut removable_positions: Vec<(i32, i32)> = Vec::new();
        for row_ix in 0..grid.len() as i32 {
            for col_ix in 0..grid[row_ix as usize].len() as i32 {
                if is_accessible(&grid, row_ix, col_ix) {
                    removable_positions.push((row_ix, col_ix));
                    removed_roll_count += 1;
                    removed_roll = true;
                }
            }
        }

        for (row_ix, col_ix) in removable_positions {
            grid[row_ix as usize][col_ix as usize] = '.';
        }
    }

    removed_roll_count
}

fn solve(input: &str) -> u32 {
    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    assert_eq!(remove_rolls_pretty(&grid), remove_rolls_simple(&grid));

    remove_rolls_simple(&grid)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
