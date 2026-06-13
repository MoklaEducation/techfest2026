## The Wormhole Priority Queue

Wormholes across the galaxy each have a travel cost. The Space Council maintains
a priority list: ships always take the cheapest available wormhole. After
processing a series of wormhole discoveries and departures, analysts need to
know the Kth smallest travel cost still available.

## Your Task
Given a list of N integers and an integer K, output the Kth smallest value
(1-indexed) in the array. Additionally output the median (middle value if N is
odd, lower-middle if N is even) of the sorted array.

### Input Specification
Line 1: T — number of queries.
Each query:
  Line 1: two integers N and K
  Line 2: N space-separated integers

### Output Specification
For each query print two space-separated values: the Kth smallest and the median.

### Sample Input
    2
    5 2
    3 1 4 1 5
    6 4
    9 3 7 1 5 2

### Sample Output
    1 3
    5 4

### Constraints
1 <= T <= 100000
1 <= K <= N <= 100000
-10^9 <= values <= 10^9
