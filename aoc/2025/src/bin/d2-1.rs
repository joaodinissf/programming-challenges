use aoc_2025::read_input;

fn is_valid(id: u64) -> bool {
    let id_str = id.to_string();

    if id_str.len() % 2 != 0 {
        return true;
    }

    let first_half = &id_str[..id_str.len() / 2];
    let second_half = &id_str[id_str.len() / 2..];

    first_half != second_half
}

fn solve(input: &str) -> String {
    let mut secret: u64 = 0;
    let mut num_invalid = 0;
    let mut total_ids = 0;

    for id_range in input.split(',') {
        let (range_start, range_end) = id_range.split_once('-').unwrap();
        let range_start: u64 = range_start.trim().parse().unwrap();
        let range_end: u64 = range_end.trim().parse().unwrap();
        for id in range_start..=range_end {
            if !is_valid(id) {
                secret += id;
                num_invalid += 1;
            }
            total_ids += 1;
        }
    }

    format!(
        "Secret: {}\n# Invalids: {}\n# Total: {}",
        secret, num_invalid, total_ids
    )
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
