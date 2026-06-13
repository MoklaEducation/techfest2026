## The Enchanted Bakery Refill Line

Grandma Plum's bakery line is enchanted. Every Kth service earns a child a magical refill, but only once. A child who gets a refill joins the back of the line. Everyone else leaves after being served.

## Your Task
Given names in arrival order and a number K, simulate the line. Every Kth service, if that child has been served only once so far, the child rejoins the back. Each child can be served at most twice. Output the order in which children finally leave.

### Input Specification
The first line contains an integer T. Each test case has two lines. The first line contains N and K. The second line contains N unique names in arrival order.

### Output Specification
For each test case, print one answer line containing the final leaving order, with names separated by comma and space.

Print one answer line per test case.

### Sample Input
    3
    4 3
    Ada Ben Cal Dee
    5 2
    A B C D E
    1 1
    Mia

### Sample Output
    Ada, Ben, Dee, Cal
    A, C, E, B, D
    Mia

### Constraints
1 <= T <= 100000. 1 <= N <= 5000. 1 <= K <= 1000. Names are unique strings of length 1 to 20.
