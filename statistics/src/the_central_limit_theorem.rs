use std::io;
use statrs::distribution::{ContinuousCDF, Normal};

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let max_weight = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let cargo_count = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let weight_avg = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let weight_stddev = parse_input!(input_line, f64);

    let total_avg = weight_avg * cargo_count;
    let total_stddev = weight_stddev * cargo_count.sqrt();

    let normal = Normal::new(total_avg, total_stddev).unwrap();
    println!("{:.4}", normal.cdf(max_weight));
}
