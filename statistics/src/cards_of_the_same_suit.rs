#![allow(non_snake_case)]

use statistics::math;
use num::rational::Ratio;

pub fn main() {
    let comb_two_cards = math::comb(52, 2);
    println!("Number of combinations of 2 cards in a deck = {}", comb_two_cards);

    let comb_two_cards_same_suit = math::comb(13, 2);
    println!("Number of combinations of️ 2 Clubs in a deck = {}", comb_two_cards_same_suit);
    println!("Number of combinations of 2 Hearts in a deck = {}", comb_two_cards_same_suit);
    println!("Number of combinations of 2 Diamonds in a deck = {}", comb_two_cards_same_suit);
    println!("Number of combinations of 2 Spades in a deck = {}", comb_two_cards_same_suit);
    println!("Number of combinations of 2 card of the same suit, all 4 suites, in a deck = {}", 4 * comb_two_cards_same_suit);

    let P_two_same_suite = Ratio::new(4 * comb_two_cards_same_suit, comb_two_cards);
    println!("Probability that 2 cards drawn from a deck without replacing are of the same suite {}",
        P_two_same_suite);
}
