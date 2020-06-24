use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    // Read N
    io::stdin().read_line(&mut input_line).unwrap();
    let _n = parse_input!(input_line, usize);
    // Read integers
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let v = input_line
        .split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();
    // Read weights
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let w = input_line
        .split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    let weighted_mean = v.iter().zip(w.iter())
        .map(|(num, weight)| *num * *weight)
        .sum::<f64>() / w.iter().sum::<f64>();
    // Mean
    println!("{:.1}", weighted_mean);
}
