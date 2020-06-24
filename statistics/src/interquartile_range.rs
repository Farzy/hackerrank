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
    let _n = parse_input!(input_line, usize);

    // Read elements
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let v = input_line
        .split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    // Read frequency
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let freq = input_line
        .split_whitespace()
        .map(|x| {
            parse_input!(x, usize)
        })
        .collect::<Vec<usize>>();

    let mut v2 : Vec<f64 >= v.iter().zip(freq.iter())
        .map(|(elt, freq)| {
            // Note: This elegant line does not work in HackerRank's Rust version
            // [*elt].repeat(*freq)

            let mut repeated_elt = vec![];
            for _ in 0..*freq {
                repeated_elt.push(*elt);
            }
            repeated_elt
        })
        .collect::<Vec<_>>()
        .concat();
    // Special sort needed for f64
    v2.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // Final vector length
    let n2 = v2.len();

    let q1 = median(&v2[0..n2 / 2]);

    let q3= if n2 % 2 == 0 {
        median(&v2[n2 / 2..])
    } else {
        median(&v2[n2 / 2 + 1..])
    };

    println!("{:.1}", q3 - q1);
}
