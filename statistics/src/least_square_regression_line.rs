use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
pub fn main() {
    let n = 5.0;
    let mut x = Vec::new();
    let mut y = Vec::new();

    for _ in 1..=5 {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let t = input_line.split_whitespace()
            .map(|x| parse_input!(*x, f64)).collect::<Vec<f64>>();
        x.push(t[0]);
        y.push(t[1]);
    }

    let sum_x = x.iter().sum::<f64>();
    let sum_y = y.iter().sum::<f64>();
    let sum_xy = x.iter().zip(&y)
        .map(|(a, b)| *a * *b).sum::<f64>();
    let sum_x_squared = x.iter()
        .map(|a| (*a).powi(2)).sum::<f64>();
    let mean_x = sum_x / n;
    let mean_y = sum_y / n;

    let b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x.powi(2));
    let a = mean_y - b * mean_x;
    println!("{:.3}", a + b * 80.0);
}
