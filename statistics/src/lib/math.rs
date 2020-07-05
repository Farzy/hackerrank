//! Mathematical and probability functions used in some
//! exercices.

/// Compute the Factorial of a positive integer `n`
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

/// Compute the number of Permutations of `r` elements from a set of `n` elements
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

/// Compute the number of Combinations of `r` elements from a set of `n` elements
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
/// If we toss a fair coin, what is the probability of getting 5 heads in a total
/// of 10 throws?
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
#[allow(dead_code)]
pub fn bidi(x : u32, n : u32, p : f64) -> f64 {
    assert_ne!(n, 0, "n should be greater than 0");
    assert!(x <= n, "x should be less than n");
    assert!(0.0 <= p, "p should be between 0 and 1");
    assert!(p <= 1.0, "p should be between 0 and 1");

    comb(n as u64, x as u64) as f64
        * p.powi(x as i32)
        * (1f64 - p).powi((n - x) as i32)
}

/// Compute the Cumulative Probability of a binomial experiment
///
/// We consider the distribution function for some real-valued random variable, `X`,
/// to be `F_X(x) = P(X <= x)`. Because this is a non-decreasing function that
/// accumulates all the probabilities for the values of `X` up to (and including) `x`,
/// we call it the cumulative distribution function (CDF) of `X`. As the CDF expresses
/// a cumulative range of values, we can use the following formula to find the
/// cumulative probabilities for all `x € [a, b]`:
///   `P(a <= X <= B) = F_X(b) - F_X(b)`
///
/// # Arguments
///
/// * `x_min`: Minimum number of successes
/// * `x_max`: Maximum number of successes
/// * `n`: Total number of trials
/// * `p`: Probability of success of 1 trial
///
/// # Examples
///
/// The probability of getting at most 5 heads is:
///
/// ```
/// use statistics::math;
///
/// let x_min = 0;
/// let x_max = 5;
/// let n = 10;
/// let p = 0.5;
///
/// let c = math::cdf(x_min, x_max, n, p);
///
/// assert_eq!(0.623046875, c);
/// ```
///
/// The probability of getting at least 5 heads is:
///
/// ```
/// use statistics::math;
///
/// let x_min = 5;
/// let x_max = 10;
/// let n = 10;
/// let p = 0.5;
///
/// let c = math::cdf(x_min, x_max, n, p);
///
/// assert_eq!(0.623046875, c);
/// ```
#[allow(dead_code)]
pub fn cdf(x_min : u32, x_max: u32, n : u32, p : f64) -> f64 {
    assert_ne!(n, 0, "n should be greater than 0");
    assert!(x_min <= x_max, "x_min should be less than x_max");
    assert!(x_max <= n, "x_max should be less than n");
    assert!(0.0 <= p, "p should be between 0 and 1");
    assert!(p <= 1.0, "p should be between 0 and 1");


    (x_min..=x_max).map(|x| comb(n as u64, x as u64) as f64
        * p.powi(x as i32)
        * (1f64 - p).powi((n - x) as i32))
        .sum()
}

/// Compute the Negative Binomial Distribution of a binomial experiment
///
/// We define a negative binomial process to be a binomial experiment meeting the following conditions:
//
/// * The number of successes is `x`
/// * The total number of trials is `n`
/// * The probability of success of 1 trial is `p`
/// * The probability of failure of 1 trial is `q`, where `q = 1 - p`.
/// * `bidi(x, n, p)` is the negative binomial probability, meaning the probability
///   of having `x - 1` success after `n - 1` trials and having `x` successes after `n` trials.
///
/// The negative binomial random variable is the number of experiments until
/// the `x`th success occurs.
///
/// The negative binomial distribution is the probability distribution for the negative binomial
/// random variable, given by the following probability mass function:
/// `negbidi(x, n, p) = comb(n-1, x-1) * p^x * q^(n-x)`
///
/// # Arguments
///
/// * `x`: Number of successes
/// * `n`: Total number of trials
/// * `p`: Probability of success of 1 trial
///
/// # Examples
///
/// If we toss a fair coin, what is the probability that at the 10th throws if
/// will have finally have 5 heads?
///
/// ```
/// use statistics::math;
///
/// let x = 5;
/// let n = 10;
/// let p = 0.5;
///
/// let nb = math::negbidi(x, n, p);
///
/// assert_eq!(0.123046875, nb);
/// ```
#[allow(dead_code)]
pub fn negbidi(x : u32, n : u32, p : f64) -> f64 {
    assert_ne!(n, 0, "n should be greater than 0");
    assert!(x <= n, "x should be less than n");
    assert!(0.0 <= p, "p should be between 0 and 1");
    assert!(p <= 1.0, "p should be between 0 and 1");

    comb((n - 1) as u64, (x - 1) as u64) as f64
        * p.powi(x as i32)
        * (1f64 - p).powi((n - x) as i32)
}

/// Geometric Distribution
///
/// The geometric distribution is a special case of the negative binomial distribution
/// that deals with the number of Bernoulli trials required to get a success (i.e.,
/// counting the number of failures before the first success).
//
/// * The total number of trials is `n`
/// * The probability of success of 1 trial is `p`
///
/// The geometric distribution is a negative binomial distribution where the number
/// of successes is 1. We express this with the following formula::
/// `geomdi(n, p) = p * q^(n-1)`
///
/// # Arguments
///
/// * `n`: Total number of trials
/// * `p`: Probability of success of 1 trial
///
/// # Examples
///
/// Bob is a high school basketball player. He is a **70%** free throw shooter, meaning
/// his probability of making a free throw is **0.7**. What is the probability that
/// Bob makes his first free throw on his fifth shot?
///
/// ```
/// use statistics::math;
///
/// let n = 5;
/// let p = 0.7;
///
/// let p_fifth = math::geomdi(n, p);
///
/// assert_eq!("0.00567", format!("{:.5}", p_fifth));
/// ```
#[allow(dead_code)]
pub fn geomdi(n : u32, p : f64) -> f64 {
    assert_ne!(n, 0, "n should be greater than 0");
    assert!(0.0 <= p, "p should be between 0 and 1");
    assert!(p <= 1.0, "p should be between 0 and 1");

    p * (1f64 - p).powi((n - 1) as i32)
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
