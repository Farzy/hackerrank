pub fn fac(n: u64) -> u64 {
    (1..=n).product()
}

pub fn perm(n: u64, r: u64) -> u64 {
    if r > n {
        0
    } else {
        ((n - r + 1)..=n).product()
    }
}

pub fn comb(n: u64, r: u64) -> u64 {
    if r > n {
        0
    } else {
        perm(n, r) / fac(r)
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn fac_0() {
        assert_eq!(1, fac(0));
    }

    #[test]
    fn fac_1() {
        assert_eq!(1, fac(1));
    }

    #[test]
    fn fac_10() {
        assert_eq!(3_628_800, fac(10));
    }

    #[test]
    fn perm_zero() {
        assert_eq!(0, perm(10, 12));
    }

    #[test]
    fn perm_equal() {
        assert_eq!(fac(10), perm(10, 10));
    }

    #[test]
    fn perm_any() {
        assert_eq!(90, perm(10, 2));
    }

    #[test]
    fn comb_zero() {
        assert_eq!(0, comb(10, 12));
    }

    #[test]
    fn comb_equal() {
        assert_eq!(1, comb(10, 10));
    }

    #[test]
    fn comb_any() {
        assert_eq!(45, comb(10, 2));
    }
}
