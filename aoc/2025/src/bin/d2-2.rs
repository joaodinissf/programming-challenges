use aoc_2025::read_input;

fn get_patterns_to_check(len: usize) -> Vec<u64> {
    let mut patterns: Vec<u64> = Vec::new();
    for size in 1..=len / 2 {
        if len % size == 0 {
            patterns.push(size as u64);
        }
    }
    patterns
}

fn is_valid_pattern(id_str: &str, pattern_size: usize) -> bool {
    let reference = &id_str[..pattern_size];
    for i in (pattern_size..id_str.len()).step_by(pattern_size) {
        let current = &id_str[i..i + pattern_size];
        if current != reference {
            return true;
        }
    }
    false
}

fn is_valid(id: u64) -> bool {
    let id_str = id.to_string();
    let patterns_to_check: Vec<u64> = get_patterns_to_check(id_str.len());

    for pattern in patterns_to_check {
        if !is_valid_pattern(&id_str, pattern as usize) {
            return false;
        }
    }
    true
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
