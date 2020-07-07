use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let sample_count = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let total_mean = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let total_stddev = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let _percentage = parse_input!(input_line, f64);

    input_line.clear();
    io::stdin().read_line(&mut input_line).unwrap();
    let z_score = parse_input!(input_line, f64);

    let sample_stddev = total_stddev / sample_count.sqrt();

    let a = total_mean - z_score * sample_stddev;
    let b = total_mean + z_score * sample_stddev;
    println!("{:.2}", a);
    println!("{:.2}", b);
}
