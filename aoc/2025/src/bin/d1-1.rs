use aoc_2025::read_input;

const MAX_POSITION: i32 = 100;

fn solve(input: &str) -> String {
    let mut secret: i32 = 0;
    let mut current_position: i32 = 50;

    for line in input.lines() {
        let mut delta = if line.get(0..1).unwrap() == "R" {
            1
        } else {
            -1
        };
        delta *= line[1..].parse::<i32>().unwrap();
        current_position = ((current_position + delta) + MAX_POSITION) % MAX_POSITION;
        if current_position == 0 {
            secret += 1;
        }
    }

    secret.to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
