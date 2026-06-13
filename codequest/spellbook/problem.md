## The Wizard's Spellbook

Aldric the Wizard checks spell formulas written with nested brackets:
( ) [ ] { }. Each opener must be closed by the matching type in correct order.
If brackets are mismatched or unclosed, the spell will backfire.

## Your Task
Given a string containing only ( ) [ ] { }, output SAFE if all brackets
are correctly matched and closed, or DANGEROUS otherwise.

### Input Specification
The first line contains T — the number of formulas to check.
Each of the next T lines contains one formula string.

### Output Specification
For each formula print SAFE or DANGEROUS.

### Sample Input
    4
    ({[]})
    ([)]
    {{{
    ()[]{} 

### Sample Output
    SAFE
    DANGEROUS
    DANGEROUS
    SAFE

### Constraints
1 <= T <= 100000
0 <= |formula| <= 10000
Formula contains only ( ) [ ] { }
