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

    fn contains(&self, ingredient: &u64) -> bool {
        match self
            .fresh_ingredients
            .binary_search_by_key(ingredient, |(start, _)| *start)
        {
            Ok(_) => true,   // Exact match found
            Err(0) => false, // ingredient is smaller than all elements
            Err(pos) => {
                // pos is where ingredient would be inserted
                // So pos-1 is the largest element <=   ingredient
                let (start, end) = self.fresh_ingredients[pos - 1];
                *ingredient >= start && *ingredient <= end
            }
        }
    }
}

fn count_fresh_ingredients(pantry: IngredientPantry, ingredients: Vec<&str>) -> u32 {
    ingredients
        .iter()
        .filter_map(|ing| ing.parse::<u64>().ok())
        .filter(|ing| pantry.contains(ing))
        .count() as u32
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
    let (pantry, ingredients_to_check) = parse_input(input);
    count_fresh_ingredients(pantry, ingredients_to_check).to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
