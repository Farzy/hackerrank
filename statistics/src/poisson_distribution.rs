use std::io;
use crate::lib::math;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let lambda =  parse_input!(input_line, f64);
    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let k = parse_input!(input_line, u32);

    // A random variable, X, follows Poisson distribution with mean of 2.5.
    // Find the probability with which the random variable X is equal to 5.
    let res = math::poisson(k, lambda);
    println!("P(k={},λ={}) = {:.3}", k, lambda, res);
}
