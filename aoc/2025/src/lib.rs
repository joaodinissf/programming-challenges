use std::error::Error;
use std::fs;

pub fn read_input(source_file: &str) -> Result<String, Box<dyn Error>> {
    let input_path = source_file.replace(".rs", ".input.txt");
    Ok(fs::read_to_string(&input_path)?)
}
