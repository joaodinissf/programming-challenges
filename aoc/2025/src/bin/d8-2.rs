use aoc_2025::read_input;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq, Ord, PartialOrd)]
struct DistanceHeapEntry {
    distance: std::cmp::Reverse<u64>,
    indices: (u32, u32),
}

#[derive(Eq, PartialEq, Ord, PartialOrd)]
struct Circuit {
    length: u64,
    members: Vec<u32>,
}

struct JunctionBoxHeap {
    boxes_xs: Vec<u32>,
    distances: BinaryHeap<DistanceHeapEntry>,
    circuits: Vec<Circuit>,
    box_to_circuit: Vec<i32>,
}

impl JunctionBoxHeap {
    fn new(junction_boxes: Vec<Vec<u32>>) -> Self {
        let n = junction_boxes.len();
        // Each junction box starts as its own circuit of size 1
        let circuits: Vec<Circuit> = (0..n)
            .map(|i| Circuit {
                length: 0,
                members: vec![i as u32],
            })
            .collect();
        let box_to_circuit: Vec<i32> = (0..n).map(|i| i as i32).collect();

        Self {
            distances: Self::populate_distances(&junction_boxes),
            circuits,
            box_to_circuit,
            boxes_xs: junction_boxes.iter().map(|b| b[0]).collect(),
        }
    }

    fn populate_distances(junction_boxes: &[Vec<u32>]) -> BinaryHeap<DistanceHeapEntry> {
        let mut distances = BinaryHeap::new();
        for i in 0..junction_boxes.len() {
            for j in i + 1..junction_boxes.len() {
                let distance = Self::get_squared_distance(&junction_boxes[i], &junction_boxes[j]);
                distances.push(DistanceHeapEntry {
                    distance,
                    indices: (i as u32, j as u32),
                });
            }
        }
        distances
    }

    fn get_squared_distance(a: &[u32], b: &[u32]) -> std::cmp::Reverse<u64> {
        std::cmp::Reverse(
            a.iter()
                .zip(b.iter())
                .map(|(x, y)| (*x as i64 - *y as i64).pow(2) as u64)
                .sum(),
        )
    }

    fn is_connected(&self, i: u32, j: u32) -> bool {
        self.box_to_circuit[i as usize] == self.box_to_circuit[j as usize]
    }

    fn connect_until_1_network(&mut self) -> u32 {
        while !self.distances.is_empty() {
            if let Some(entry) = self.distances.pop() {
                let (i, j) = entry.indices;
                let distance = entry.distance.0;

                // Check if the indices are already in the same circuit, nothing to do
                if self.is_connected(i, j) {
                    continue;
                }

                // Merge the two circuits
                let ci = self.box_to_circuit[i as usize];
                let cj = self.box_to_circuit[j as usize];

                let cj_members = std::mem::take(&mut self.circuits[cj as usize].members);
                let cj_length = self.circuits[cj as usize].length;

                for &member in &cj_members {
                    self.box_to_circuit[member as usize] = ci;
                }

                self.circuits[ci as usize].members.extend(cj_members);
                self.circuits[ci as usize].length += cj_length + distance;

                let last_idx = self.circuits.len() - 1;
                if cj as usize != last_idx {
                    for &member in &self.circuits[last_idx].members {
                        self.box_to_circuit[member as usize] = cj;
                    }
                }
                self.circuits.swap_remove(cj as usize);

                if self.circuits.len() == 1 {
                    return self.boxes_xs[i as usize] * self.boxes_xs[j as usize] as u32;
                }
            }
        }
        0
    }
}

fn parse_input(input: &str) -> Vec<Vec<u32>> {
    input
        .lines()
        .filter_map(|line| {
            Some(
                line.split(',')
                    .filter_map(|s| s.trim().parse().ok())
                    .collect(),
            )
        })
        .collect()
}

fn solve(input: &str) -> String {
    let junction_boxes = parse_input(input);
    let mut junction_boxes = JunctionBoxHeap::new(junction_boxes);

    junction_boxes.connect_until_1_network().to_string()
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = read_input(file!())?;
    let result = solve(&contents);
    println!("{}", result);
    Ok(())
}
