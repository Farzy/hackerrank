mod template;
mod basic_statistics;
mod weighted_mean;
mod standard_deviation;
mod quartiles;
mod interquartile_range;

use std::collections::HashMap;
use std::env;
use statistics::helper;

// Simplify long hashmap type
type FunctionHash = HashMap<String, (String, fn())>;

fn usage(functions: &FunctionHash) {
    eprintln!(r#"
Usage: PROGNAME [options] function

 -h: Print this help

Specify one function name.

List of functions:"#);
    for (name, (description, _)) in functions {
        eprintln!(" - {}: {}", name, description);
    }
}

fn main() {
    let mut functions: FunctionHash = HashMap::new();
    functions.insert(String::from("basic-statistics"), (String::from("Basic statistics"), basic_statistics::main));
    functions.insert(String::from("weighted-mean"), (String::from("Weighted mean"), weighted_mean::main));
    functions.insert(String::from("standard-deviation"), (String::from("Standard deviation"), standard_deviation::main));
    functions.insert(String::from("quartiles"), (String::from("Quartiles"), quartiles::main));
    functions.insert(String::from("interquartile-range"), (String::from("Interquartile range"), interquartile_range::main));

    if env::args().len() != 2 { // No arguments or too many
        usage(&functions);
    } else {
        for k in env::args().skip(1) {
            if k == "-h" || k == "--help" {
                usage(&functions);
                return;
            } else if functions.contains_key(&k) {
                let (description, func) = functions.get(&k).unwrap();
                helper::section(description);
                func();
            } else {
                eprintln!("\nERROR: Function '{}' not found", k);
            }
        }
    }
}
