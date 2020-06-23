use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[allow(dead_code)]
fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();

    let temp_min = 0i32;
    for i in inputs.split_whitespace() {
        let t = parse_input!(i, i32);
        if t.abs() < temp_min.abs() || (t > 0 && t + temp_min == 0) {
            ();
        }
    }

    println!("{}", n);
}
