pub struct Solution;

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut left = match s.chars().nth(0).unwrap() {
            '0' => 1,
            _ => 0,
        };
        let mut right = 0;

        for c in s.chars().skip(1) {
            if c == '1' {
                right += 1;
            }
        }

        let mut max_score = left + right;
        s.chars().enumerate().for_each(|(i, c)| {
            if i == 0 || i == s.len() - 1 {
                return;
            }

            if c == '0' {
                left += 1;
            } else {
                right -= 1;
            }

            if left + right > max_score {
                max_score = left + right;
            }
        });

        max_score
    }
}
