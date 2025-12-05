use aoc_2025::read_input;

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

fn solve(input: &str) -> u32 {
    let mut accessible_count: u32 = 0;

    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    for row_ix in 0..grid.len() as i32 {
        for col_ix in 0..grid[row_ix as usize].len() as i32 {
            accessible_count += is_accessible(&grid, row_ix, col_ix) as u32;
        }
    }

    accessible_count
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
