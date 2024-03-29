use std::io;
use statrs::distribution::{ContinuousCDF, Normal};

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
pub fn main() {
    let mut input_line = String::new();

    io::stdin().read_line(&mut input_line).unwrap();
    let mut input_iter = input_line.split_whitespace();
    let mean = parse_input!(input_iter.next().unwrap(), f64);
    let sd = parse_input!(input_iter.next().unwrap(), f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let q1 = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    input_iter = input_line.split_whitespace();
    let q2_1 = parse_input!(input_iter.next().unwrap(), f64);
    let q2_2 = parse_input!(input_iter.next().unwrap(), f64);

    let normal = Normal::new(mean, sd).unwrap();
    println!("{:.3}", normal.cdf(q1));
    println!("{:.3}", normal.cdf(q2_2) - normal.cdf(q2_1));
}
