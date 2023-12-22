// https://leetcode.com/problems/unique-paths/

pub struct Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let rows = m as usize;
        let cols = n as usize;
        let mut matrix = vec![vec![1; cols]; rows];

        for i in 1..rows {
            for j in 1..cols {
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
            }
        }

        matrix[rows - 1][cols - 1]
    }
}
