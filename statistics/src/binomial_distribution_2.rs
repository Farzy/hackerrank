use std::io;
use crate::lib::math;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut ratios =  input_line.split_whitespace();
    let p_incorrect_size = parse_input!(ratios.next().unwrap(), f64) / 100.0;
    let batch_size = parse_input!(ratios.next().unwrap(), u32);

    // What is the probability that a batch of 10 pistons will contain no more than 2 rejects?
    let res = math::cdf(0, 2, batch_size, p_incorrect_size);
    println!("P(rejects <= 2) = {:.3}", res);
    // What is the probability that a batch of 10 pistons will contain at least 2 rejects?
    let res = math::cdf(2, batch_size, batch_size, p_incorrect_size);
    println!("P(rejects >= 2) = {:.3}", res);
}
