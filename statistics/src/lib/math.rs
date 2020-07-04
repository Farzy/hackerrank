//! Mathematical and probability functions used in some
//! exercices.

/// Compute the Factorial of a positive integer
///
/// # Examples
///
/// ```
/// use statistics::math;
///
/// let n = 5;
/// let fac5 = math::fac(5);
///
/// assert_eq!(fac5, 120);
/// ```
pub fn fac(n: u64) -> u64 {
    (1..=n).product()
}

/// Compute the number of Permutations of r elements from a set of n elements
///
/// # Examples
///
/// ```
/// use statistics::math;
///
/// let n = 5;
/// let r = 3;
/// let perm_3_5 = math::perm(n, r);
///
/// assert_eq!(perm_3_5, 60);
/// ```
pub fn perm(n: u64, r: u64) -> u64 {
    if r > n {
        0
    } else {
        ((n - r + 1)..=n).product()
    }
}

/// Compute the number of Combinations of r elements from a set of n elements
///
/// # Examples
///
/// ```
/// use statistics::math;
///
/// let n = 5;
/// let r = 3;
/// let comb_3_5 = math::comb(n, r);
///
/// assert_eq!(comb_3_5, 10);
/// ```
pub fn comb(n: u64, r: u64) -> u64 {
    if r > n {
        0
    } else {
        perm(n, r) / fac(r)
    }
}

/// Compute the Binomial Distribution of a binomial experiment
///
/// We define a binomial process to be a binomial experiment meeting the following conditions:
//
/// * The number of successes is `x`
/// * The total number of trials is `n`
/// * The probability of success of 1 trial is `p`
/// * The probability of failure of 1 trial is `q`, where `q = 1 - p`.
/// * `bidi(x, n, p)` is the binomial probability, meaning the probability of having exactly
/// `x` successes out of `n` trials.
///
/// The binomial random variable is the number of successes, `x`, out of `n` trials.
///
/// The binomial distribution is the probability distribution for the binomial random variable,
/// given by the following probability mass function:
/// `bidi(x, n, p) = comb(n, x) * p^x * q^(n-x)`
///
/// # Arguments
///
/// * `x`: Number of successes
/// * `n`: Total number of trials
/// * `p`: Probability of success of 1 trial
///
/// # Examples
///
/// ```
/// use statistics::math;
///
/// let x = 5;
/// let n = 10;
/// let p = 0.5;
///
/// let b = math::bidi(x, n, p);
///
/// assert_eq!(0.24609375, b);
/// ```
pub fn bidi(x : u32, n : u32, p : f64) -> f64 {
    assert_ne!(n, 0, "n should be greater than 0");
    assert_ne!(x, 0, "x should be greater than 0");
    assert!(x <= n, "x should be less than n");
    assert!(0.0 <= p, "p should be between 0 and 1");
    assert!(p <= 1.0, "p should be between 0 and 1");

    comb(n as u64, x as u64) as f64
        * p.powi(x as i32)
        * (1f64 - p).powi((n - x) as i32)
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

    #[test]
    fn bidi_all_args_ok() {
        let res = bidi(1, 2, 0.5);
        assert_eq!(0.5, res);
    }

    #[test]
    #[should_panic]
    fn bidi_x_greater_n() {
        let _res = bidi(5, 4, 0.5);
    }

    #[test]
    #[should_panic]
    fn bidi_p_ge_0() {
        let _res = bidi(3, 4, -1.0);
    }

    #[test]
    #[should_panic]
    fn bidi_p_le_1() {
        let _res = bidi(3, 4, 1.1);
    }
}
