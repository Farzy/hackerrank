use std::io;
use std::collections::HashMap;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

pub fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, usize);

    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();
    let mut map = HashMap::new(); // For counting occurrences
    let mut map_max = 0; // For keeping the highest occurrence
    let mut v = inputs
        .split_whitespace()
        .map(|x| {
            // Ugly: we populate "map" using a side effect in map() iterator…
            let entry = map.entry(parse_input!(x, i32)).or_insert(0);
            *entry += 1;
            // Helper to find "mode" of entries
            if *entry > map_max {
                map_max = *entry;
            }
            // Now populate "v"
            parse_input!(x, f64)
        })
        .collect::<Vec<f64>>();

    // Special sort needed for f64
    v.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // Mean
    println!("{:.1}", v.iter().sum::<f64>() / n as f64);
    // Average
    if n % 2 == 0 {
        println!("{}", (v[n/2 - 1] + v[n/2]) / 2.0);
    } else {
        println!("{}", v[n/2])
    }
    // Mode
    map.retain(|_, v| *v == map_max); // Keep entries with count == mode
    let mode = map.keys().min().unwrap();
    println!("{}", mode);
}
