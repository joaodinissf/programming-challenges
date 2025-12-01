use aoc_2025::read_input;

const MAX_POSITION: i32 = 100;

fn solve(input: &str) -> String {
    let mut secret: i32 = 0;
    let mut current_position: i32 = 50;
    for line in input.lines() {
        let old_position = current_position;
        let mut delta = if line.get(0..1).unwrap() == "R" {
            1
        } else {
            -1
        };
        delta *= line[1..].parse::<i32>().unwrap();

        secret += delta.abs() / MAX_POSITION;
        delta %= MAX_POSITION;

        current_position += delta;
        if (current_position >= MAX_POSITION) || (current_position <= 0 && old_position > 0) {
            secret += 1;
        }

        current_position = current_position.rem_euclid(MAX_POSITION);
    }
    secret.to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);

    println!("{}", result);

    Ok(())
}
