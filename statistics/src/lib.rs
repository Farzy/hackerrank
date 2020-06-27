pub mod helper {
    pub fn section(title: &str) {
        let len = title.len();
        let dashes = "-".repeat(len);
        println!("\n+-{}-+", dashes);
        println!("| {} |", title);
        println!("+-{}-+", dashes);
    }

    pub fn subsection(title: &str) {
        let len = title.len();
        let dashes = "-".repeat(len+1);
        println!("\n{}:", title);
        println!("{}\n", dashes);
    }
}

pub mod math {
    pub fn fac(n: u64) -> u64 {
        (1..=n).product()
    }

    pub fn perm(n: u64, r: u64) -> u64 {
        if r > n {
            0
        } else {
            fac(n) / fac(n - r)
        }
    }

    pub fn comb(n: u64, r: u64) -> u64 {
        if r > n {
            0
        } else {
            fac(n) / fac(n - r) / fac(r)
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn fac_0() {
        assert_eq!(1, math::fac(0));
    }

    #[test]
    fn fac_1() {
        assert_eq!(1, math::fac(1));
    }

    #[test]
    fn fac_10() {
        assert_eq!(3_628_800, math::fac(10));
    }

    #[test]
    fn perm_zero() {
        assert_eq!(0, math::perm(10, 12));
    }

    #[test]
    fn perm_equal() {
        assert_eq!(math::fac(10), math::perm(10, 10));
    }

    #[test]
    fn perm_any() {
        assert_eq!(90, math::perm(10, 2));
    }

    #[test]
    fn comb_zero() {
        assert_eq!(0, math::comb(10, 12));
    }

    #[test]
    fn comb_equal() {
        assert_eq!(1, math::comb(10, 10));
    }

    #[test]
    fn comb_any() {
        assert_eq!(45, math::comb(10, 2));
    }
}
