use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut x_y = input_line.split_whitespace();
    let a_lambda =  parse_input!(x_y.next().unwrap(), f64);
    let b_lambda = parse_input!(x_y.next().unwrap(), f64);

    // We have to calculate the Expectation for the random variable X squared.
    // There is not enough explanation in the tutorial…
    let ca = 160.0 + 40.0 * (a_lambda + a_lambda.powi(2));
    let cb = 128.0 + 40.0 * (b_lambda + b_lambda.powi(2));
    println!("{:.3}", ca);
    println!("{:.3}", cb);
}
