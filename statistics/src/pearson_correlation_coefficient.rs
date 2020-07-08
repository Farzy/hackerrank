use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn mean(values: &[f64]) -> f64 {
    values.iter().sum::<f64>() / values.len() as f64
}

fn std_dev(values: &[f64]) -> f64 {
    let m = mean(values);
    (values.iter()
        .map(|x| (*x - m).powi(2))
        .sum::<f64>()
        / (values.len() as f64)).sqrt()
}

fn covariance(values_x: &[f64], values_y: &[f64]) -> f64 {
    assert_eq!(values_x.len(), values_y.len(), "Both arrays must be the same size");

    let mean_x = mean(values_x);
    let mean_y = mean(values_y);
    values_x.iter().zip(values_y)
        .map(|(x, y)| (*x - mean_x) * (*y - mean_y))
        .sum::<f64>() / values_x.len() as f64
}

#[allow(dead_code)]
pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let _n = parse_input!(input_line, i32);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let values_x = input_line.split_whitespace()
        .map(|x| parse_input!(*x, f64)).collect::<Vec<f64>>();

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let values_y = input_line.split_whitespace()
        .map(|x| parse_input!(*x, f64)).collect::<Vec<f64>>();

    let std_dev_x = std_dev(&values_x);
    let std_dev_y = std_dev(&values_y);
    let pearson_correlation_coef = covariance(&values_x, &values_y)
        / std_dev_x / std_dev_y;
    println!("{:.3}", pearson_correlation_coef);
}
