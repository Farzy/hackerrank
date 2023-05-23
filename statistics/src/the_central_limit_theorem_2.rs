use std::io;
use statrs::distribution::{ContinuousCDF, Normal};

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let max_tickets = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let students_count = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let tickets_avg = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let tickets_stddev = parse_input!(input_line, f64);

    let total_tickets_avg = tickets_avg * students_count;
    let total_tickets_stddev = tickets_stddev * students_count.sqrt();

    let normal = Normal::new(total_tickets_avg, total_tickets_stddev).unwrap();
    println!("{:.4}", normal.cdf(max_tickets));
}
