use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn median(v: &[f64]) -> f64 {
    let n = v.len();
    if n % 2 == 0 {
        (v[n/2 - 1] + v[n/2]) / 2.0
    } else {
        v[n/2]
    }
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, usize);

    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();
    let mut v = inputs
        .split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    // Special sort needed for f64
    v.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // Median
    let q2= median(&v);

    let q1 = median(&v[0..n / 2]);

    let q3= if n % 2 == 0 {
        median(&v[n / 2..])
    } else {
        median(&v[n / 2 + 1..])
    };

    println!("{:.0}\n{:.0}\n{:.0}", q1, q2, q3);
}
