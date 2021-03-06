extern crate num;

mod lib;
mod template;
mod basic_statistics;
mod weighted_mean;
mod standard_deviation;
mod quartiles;
mod interquartile_range;
mod compound_event_probability;
mod cards_of_the_same_suit;
mod conditional_probability;
mod binomial_distribution;
mod binomial_distribution_2;
mod geometric_distribution;
mod geometric_distribution_2;
mod poisson_distribution;
mod poisson_distribution_2;
mod normal_distribution;
mod normal_distribution_2;
mod the_central_limit_theorem;
mod the_central_limit_theorem_2;
mod the_central_limit_theorem_3;
mod pearson_correlation_coefficient;
mod spearman_rank_correlation_coefficient;
mod least_square_regression_line;

use std::collections::HashMap;
use std::env;
use crate::lib::helper;

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
    functions.insert(String::from("compound-event-probability"), (String::from("Compound Event Probability"), compound_event_probability::main));
    functions.insert(String::from("cards-of-the-same-suit"), (String::from("Cards of the same suite"), cards_of_the_same_suit::main));
    functions.insert(String::from("conditional-probability"), (String::from("Conditional Probability"), conditional_probability::main));
    functions.insert(String::from("binomial-distribution"), (String::from("Binomial Distribution"), binomial_distribution::main));
    functions.insert(String::from("binomial-distribution-2"), (String::from("Binomial Distribution 2"), binomial_distribution_2::main));
    functions.insert(String::from("geometric-distribution"), (String::from("Geometric Distribution "), geometric_distribution::main));
    functions.insert(String::from("geometric-distribution-2"), (String::from("Geometric Distribution 2"), geometric_distribution_2::main));
    functions.insert(String::from("poisson-distribution"), (String::from("Poisson Distribution"), poisson_distribution::main));
    functions.insert(String::from("poisson-distribution-2"), (String::from("Poisson Distribution 2"), poisson_distribution_2::main));
    functions.insert(String::from("normal-distribution"), (String::from("Normal Distribution"), normal_distribution::main));
    functions.insert(String::from("normal-distribution-2"), (String::from("Normal Distribution 2"), normal_distribution_2::main));
    functions.insert(String::from("the-central-limit-theorem"), (String::from("The Central Limit Theorem"), the_central_limit_theorem::main));
    functions.insert(String::from("the-central-limit-theorem-2"), (String::from("The Central Limit Theorem 2"), the_central_limit_theorem_2::main));
    functions.insert(String::from("the-central-limit-theorem-3"), (String::from("The Central Limit Theorem 3"), the_central_limit_theorem_3::main));
    functions.insert(String::from("pearson-correlation-coefficient"), (String::from("Pearson Correlation Coefficient"), pearson_correlation_coefficient::main));
    functions.insert(String::from("spearman-rank-correlation-coefficient"), (String::from("Spearman Rank Correlation Coefficient"), spearman_rank_correlation_coefficient::main));
    functions.insert(String::from("least-square-regression-line"), (String::from("Least Square Regression Line"), least_square_regression_line::main));

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
