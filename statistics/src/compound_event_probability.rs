#![allow(non_snake_case)]

use num::rational::Ratio;

pub fn main() {
    let P_Xr = Ratio::new(4, 4 + 3);
    println!("Probability to pick a Red ball from Urn X   P(Xr) = {}", P_Xr);

    let P_Xb = Ratio::from(1) - P_Xr;
    println!("Probability to pick a Black ball from Urn X P(Xb) = {}", P_Xb);

    let P_Yr = Ratio::new(5, 5 + 4);
    println!("Probability to pick a Red ball from Urn Y   P(Yr) = {}", P_Yr);

    let P_Yb = Ratio::from(1) - P_Yr;
    println!("Probability to pick a Black ball from Urn Y P(Yb) = {}", P_Yb);

    let P_Zr = Ratio::new(4, 4 + 4);
    println!("Probability to pick a Red ball from Urn Z   P(Zr) = {}", P_Zr);

    let P_Zb = Ratio::from(1) - P_Zr;
    println!("Probability to pick a Black ball from Urn Z P(Zb) = {}", P_Zb);

    println!("These probabilities are independent. Therefore the probability to pick R, R, B is");
    println!("the product of P(Xr), P(Yr) and P(Zb):");
    let P_RRB = P_Xr * P_Yr * P_Zb;
    println!("P(R,R,B) = {}", P_RRB);
    println!("And so on…");
    let P_RBR = P_Xr * P_Yb * P_Zr;
    println!("P(R,B,R) = {}", P_RBR);
    let P_BRR = P_Xb * P_Yr * P_Zr;
    println!("P(B,R,R) = {}", P_BRR);

    println!("These 3 probabilities are mutually exclusive, therefore P(2 Red, 1 Black) = P(R,R,B) + P(R,B,R) + P(B,R,R)");
    let P_total = P_RRB + P_RBR + P_BRR;
    println!("P(2 Red, 1 Black) = {}", P_total);
}
