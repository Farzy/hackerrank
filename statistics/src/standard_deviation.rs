use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    // Read N
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, usize);
    // Read integers
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let v = input_line
        .split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    // Mean
    let mean = v.iter().sum::<f64>() / n as f64;
    // Standard deviation
    let standard_deviation = ((v.iter()
        .map(|x| (*x - mean).powi(2))
        .sum::<f64>()) / n as f64).sqrt();
    println!("{:.1}", standard_deviation);
}
