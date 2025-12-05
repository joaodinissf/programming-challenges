use aoc_2025::read_input;

struct IngredientPantry {
    fresh_ingredients: Vec<(u64, u64)>,
}

impl IngredientPantry {
    fn new() -> Self {
        IngredientPantry {
            fresh_ingredients: Vec::new(),
        }
    }

    fn add_fresh_ingredient_range(&mut self, start: u64, end: u64) {
        self.fresh_ingredients.push((start, end));
    }

    fn compact_ranges(&mut self) {
        self.fresh_ingredients.sort_unstable();
        for i in (1..self.fresh_ingredients.len()).rev() {
            let (_prev_start, prev_end) = self.fresh_ingredients[i - 1];
            let (curr_start, curr_end) = self.fresh_ingredients[i];
            if prev_end + 1 >= curr_start {
                self.fresh_ingredients[i - 1].1 = prev_end.max(curr_end);
                self.fresh_ingredients.remove(i);
            }
        }
    }
}

fn get_total_fresh_ingredients(pantry: IngredientPantry) -> u64 {
    pantry
        .fresh_ingredients
        .iter()
        .map(|(start, end)| end - start + 1)
        .sum::<u64>()
}

fn parse_input(input: &str) -> (IngredientPantry, Vec<&str>) {
    let mut pantry = IngredientPantry::new();
    for line in input.lines() {
        if line.trim().is_empty() {
            pantry.compact_ranges();
            break;
        }
        let parts: Vec<&str> = line.split('-').collect();
        let start: u64 = parts[0].trim().parse().unwrap();
        let end: u64 = parts[1].trim().parse().unwrap();
        pantry.add_fresh_ingredient_range(start, end);
    }

    let ingredients_to_check: Vec<&str> = input
        .lines()
        .skip_while(|line| !line.trim().is_empty())
        .skip(1)
        .collect();

    (pantry, ingredients_to_check)
}

fn solve(input: &str) -> String {
    let (pantry, _) = parse_input(input);
    get_total_fresh_ingredients(pantry).to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
