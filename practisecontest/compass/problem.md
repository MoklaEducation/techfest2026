## The Magic Compass Walk

A young explorer has a magic compass that records every step as a letter.`N` means one step north, `S` means one step south, `E` means one step east, and `W` means one step west. After walking, the explorer wants to know the final position and how far away it is from the starting point using city-block distance. Explorer always starts from the location `(0,0)`

## Your Task
Given a string of compass letters, calculate the final `(x, y)` position. East increases `x`, west decreases `x`, north increases `y`, and south decreases `y`. Also calculate the distance `abs(x) + abs(y)`.

### Input Specification
The first line will contain an integer ~N~ specifying how many walks need to be checked.
The next ~N~ lines will each contain one string made only of the letters `N`, `S`, `E`, and `W`.

### Output Specification
For each test case, output `Position = (X, Y), Distance = D`. All values are integers.

### Sample Input
    3
    NNEESSW
    WWNN
    NESW


### Sample Output
    Position = (1, 0), Distance = 1
    Position = (-2, 2), Distance = 4
    Position = (0, 0), Distance = 0
