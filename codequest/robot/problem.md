## The Robot Vacuum Map

A tiny robot vacuum cleans the wizard's tiled room. It can turn left or right and move forward, but if it tries to leave the room, it bumps the wall and stays in place.

## Your Task
Given room size R by C, a starting row, column, and direction, and commands F, L, R, simulate the robot. Rows and columns are 1-based. F moves one square forward if the square is inside the room; otherwise the robot stays put.

### Input Specification
The first line will contain an integer ~T~ specifying how many test cases will be checked.
For each test case, one line contains R and C. The next line contains starting row, starting column, and direction. The next line contains the command string.
Print one answer line per test case.

### Output Specification
For each test case, print Final = (row, col, direction).

### Constraints
1 <= R, C <= 1000. 1 <= command length <= 100000.

### Sample Input
    3
    3 3
    2 2 N
    FFRFF
    2 2
    1 1 E
    RFLF
    2 2
    2 2 S
    F


### Sample Output
    Final = (1, 3, E)
    Final = (2, 2, E)
    Final = (2, 2, S)
