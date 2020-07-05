use std::io;
use crate::lib::math;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let ratios =  input_line.split_whitespace()
        .map(|x| {
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    // Ratio of boy vs girl at birth
    let ratio_boy = ratios[0];
    let ratio_girl = ratios[1];
    let p_boy =  ratio_boy / (ratio_boy + ratio_girl);
    println!("Ratio boy/girl {} : {} -> P(boy): {}", ratio_boy, ratio_girl, p_boy);

    // What proportion of Russian families with exactly 6 children will have at least 3 boys?
    let res = math::cdf(3, 6, 6, p_boy);
    println!("P(boy >= 3) = {:.3}", res);
}

