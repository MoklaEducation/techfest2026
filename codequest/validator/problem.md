## The Nav-Computer Validator

The navigation computer on starship Helios accepts route coordinates as
IPv4-style addresses (four dot-separated integers each in 0-255). A faulty
input parser sometimes sends corrupted strings. Before plotting any course,
the validator must check each coordinate string.

Rules for a VALID coordinate string:
  - Exactly 4 groups separated by exactly 3 dots
  - Each group contains only digits
  - No group has leading zeros (unless the group is exactly "0")
  - Each group's value is between 0 and 255 inclusive

## Your Task
Given a string, output VALID or INVALID.

### Input Specification
Line 1: T — number of strings to validate.
Each of the next T lines: one coordinate string.

### Output Specification
For each string print VALID or INVALID.

### Sample Input
    5
    192.168.1.1
    256.0.0.1
    192.168.01.1
    0.0.0.0
    1.2.3

### Sample Output
    VALID
    INVALID
    INVALID
    VALID
    INVALID

### Constraints
1 <= T <= 200000
1 <= string length <= 20
Strings contain printable ASCII characters.
