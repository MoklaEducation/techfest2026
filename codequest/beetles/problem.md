## The Unique Scarab Beetles

Collector Amentet wants only unique scarab amulets displayed in the royal
exhibition. She needs the count of distinct values and the distinct values
listed in their first-appearance order.

## Your Task
Given N integers, output the count of distinct values followed by the distinct
values in the order they first appeared.

### Input Specification
The first line contains T — the number of collections to process.
Each collection begins with N on its own line, followed by N space-separated integers.

### Output Specification
For each collection print two lines:
  Count: <number of distinct values>
  <distinct values in first-appearance order, space-separated>

### Sample Input
    2
    7
    3 1 4 1 5 9 3
    4
    7 7 7 7

### Sample Output
    Count: 5
    3 1 4 5 9
    Count: 1
    7

### Constraints
1 <= T <= 10000
1 <= N <= 10000
1 <= each value <= 10000
