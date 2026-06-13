## The Flood Season Harvest

After the Nile floods recede, farmers measure their grain harvest in baskets.
The vizier needs the total grain and the floor of the average per farm for
the Pharaoh's official records.

## Your Task
Given N integers (grain counts), output the total sum and the floor of the
average (integer division: sum / N).

### Input Specification
The first line contains an integer T — the number of reports.
Each report starts with N on its own line, followed by N space-separated integers.

### Output Specification
For each report print two lines:
  Total: <sum>
  Average: <floor(sum/N)>

### Sample Input
    2
    4
    10 20 30 40
    3
    7 8 9

### Sample Output
    Total: 100
    Average: 25
    Total: 24
    Average: 8

### Constraints
1 <= T <= 10000
1 <= N <= 10000
1 <= each value <= 100000
