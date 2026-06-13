## The Tower of Ancient Stones

Blocks arrive one at a time. A block is placed on the tower only if it is
strictly smaller than the current top block (the first block always goes on).
Otherwise it is added to the discard pile. Output the discard pile contents
in first-discarded to last-discarded order. If the pile is empty, output
EMPTY DISCARD.

## Your Task
Given N blocks arriving in a specified order, simulate the tower placement
rule and output the discard pile.

### Input Specification
The first line contains T — the number of simulations.
Each simulation starts with N on its own line, followed by N space-separated
integers (block values in arrival order).

### Output Specification
For each simulation print the discarded values space-separated, or EMPTY DISCARD.

### Sample Input
    2
    5
    3 1 4 2 5
    4
    4 3 2 1

### Sample Output
    4 2 5
    EMPTY DISCARD

### Constraints
1 <= T <= 100000
1 <= N <= 10000
All block values are distinct positive integers.
