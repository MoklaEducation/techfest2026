## The Carnival Ticket Machine

Children line up for tickets. VIP children (golden hats) are always served
before NORMAL children. Among the same type, earlier arrivals go first.
Output the order in which all children are served.

## Your Task
Given N children each tagged VIP or NORMAL, output their names in service
order (all VIPs in arrival order first, then all NORMALs in arrival order).

### Input Specification
The first line contains T — the number of carnival days.
Each day starts with N on its own line, followed by N lines each containing
a name and type (VIP or NORMAL) separated by a space.

### Output Specification
For each day print the names in service order, one per line.

### Sample Input
    1
    4
    Alice NORMAL
    Bob VIP
    Carol NORMAL
    Dave VIP

### Sample Output
    Bob
    Dave
    Alice
    Carol

### Constraints
1 <= T <= 1000
1 <= N <= 10000
Names are unique strings of up to 30 characters.
Type is exactly VIP or NORMAL.
