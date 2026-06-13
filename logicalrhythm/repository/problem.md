## The Sacred Scroll Repository

The Repository Keeper Thoth-Mes has arranged every scroll in strict numerical
order. When a scholar requests scroll number T, Thoth-Mes uses a clever halving
strategy: check the middle, then discard the wrong half. Repeat until found or
declared lost.

## Your Task
Given a sorted array of N distinct integers and a target T, output the 0-based
index of T. If T is not found, output -1.
You must solve this using binary search.

### Input Specification
The first line contains Q — the number of queries.
Each query consists of two lines:
  Line 1: two integers N and T
  Line 2: N space-separated integers in sorted (ascending) order

### Output Specification
For each query print one line: the 0-based index or -1.

### Sample Input
    3
    7 14
    2 5 8 12 14 23 38
    5 10
    1 3 5 7 9
    4 25
    10 20 30 40

### Sample Output
    4
    -1
    -1

### Constraints
1 <= Q <= 100000
1 <= N <= 100000
All values in each array are distinct.
1 <= T <= 1000000
