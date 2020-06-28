pub fn main() {
    println!(r#"Sample space : There are 2 kids, 2 sex (M, F), the space is {{M, F}} x {{M, F}}

Event B = a kid is a boy {{M}}
P(B) = 3/4

Event T = The 2 kids are boys {{M, M}}
P(T) = 1/4

P(T\B) = P(T^B) / P(B)
       = P(B\T) * P(T) / P(B)
       = 1 * 1/4 / 3/4
       = 1/3
"#)
}
