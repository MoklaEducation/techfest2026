## The Nebula Scanner

Aboard the ISS Prometheus, the nebula scanner captures energy readings
every second stored in an array. Scientists want to analyse the peak energy
in every consecutive window of K seconds — a sliding maximum across the
entire reading sequence.

## Your Task
Given N energy readings and window size K, output the maximum value in each
consecutive window of size K. There are N-K+1 windows total.

### Input Specification
Line 1: T — number of scan sequences.
Each sequence:
  Line 1: two integers N and K
  Line 2: N space-separated integers

### Output Specification
For each sequence print N-K+1 space-separated integers: the maximum of each
window.

### Sample Input
    2
    8 3
    1 3 -1 -3 5 3 6 7
    5 2
    4 3 5 1 2

### Sample Output
    3 3 5 5 6 7
    4 5 5 2

### Constraints
1 <= T <= 10000
1 <= K <= N <= 100000
-10^9 <= each value <= 10^9
