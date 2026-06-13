## The Potion Shelf

Mira the Witch keeps potions on a shelf, each with a power level. She needs
the second most powerful potion (second largest DISTINCT value) as a backup.
If no second distinct value exists, output NO BACKUP.

## Your Task
Given N integers (potion power levels), find the second largest distinct value.
If none exists, output NO BACKUP.

### Input Specification
The first line contains T — the number of shelves.
Each shelf starts with N on its own line, followed by N space-separated integers.

### Output Specification
For each shelf print the second largest distinct value, or NO BACKUP.

### Sample Input
    2
    5
    5 3 9 7 9
    3
    4 4 4

### Sample Output
    7
    NO BACKUP

### Constraints
1 <= T <= 100000
2 <= N <= 10000
1 <= each value <= 1000000
