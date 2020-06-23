use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, usize);

    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();
    let mut v = inputs
        .split_whitespace()
        .map(|x| parse_input!(x, f64))
        .collect::<Vec<f64>>();
    v.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // Mean
    println!("{:.1}", v.iter().sum::<f64>() / n as f64);
    // Average
    if n % 2 == 0 {
        println!("{}", (v[n/2 - 1] + v[n/2]) / 2.0);
    } else {
        println!("{}", v[n/2])
    }
    // Mode
}
