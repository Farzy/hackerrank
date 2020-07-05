use std::io;
use crate::lib::math;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut ratio_defect =  input_line.split_whitespace();
    let mut p_defect = parse_input!(ratio_defect.next().unwrap(), f64);
    p_defect /= parse_input!(ratio_defect.next().unwrap(), f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let inspections = parse_input!(input_line, u32);

    // The probability that a machine produces a defective product is 1/3.
    // What is the probability that the 1st defect is found during the first 5th inspections?
    // The probabilities of finding the defect during the Nth inspection or the Mth inspection
    // are mutually exclusive. We can therefore add individual probabilities.
    let res = (1..=inspections).map(|inspection| math::geomdi(inspection, p_defect)).sum::<f64>();
    println!("P(1st defect on first 5th inspection) = {:.3}", res);
}
