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

fn rank(value: f64, sorted_unique_values: &[f64]) -> usize {
    for x in sorted_unique_values.iter().enumerate() {
        if *x.1 == value {
            return x.0 +1;
        }
    }
    0
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

    let  mut x_sorted = values_x.clone();
    x_sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    x_sorted.dedup();
    let x_rank = values_x
        .iter()
        .map(|x| rank(*x, &x_sorted) as f64)
        .collect::<Vec<_>>();

    let mut y_sorted = values_y.clone();
    y_sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    y_sorted.dedup();
    let y_rank = values_y
        .iter()
        .map(|x| rank(*x, &y_sorted) as f64)
        .collect::<Vec<_>>();

    // println!("{:?} sorts to {:?}", values_x, x_rank);
    // println!("{:?} sorts to {:?}", values_y, y_rank);

    let std_dev_x = std_dev(&x_rank);
    let std_dev_y = std_dev(&y_rank);
    let pearson_correlation_coef = covariance(&x_rank, &y_rank)
        / std_dev_x / std_dev_y;
    println!("{:.3}", pearson_correlation_coef);
}
