## The Goblin Snack Boxes

A group of goblins is sorting snack boxes before a forest party. They want to know two things: the total number of snacks in boxes that have an even number of snacks, and how many boxes are big enough to have at least a special number of snacks.

## Your Task
Given the snack count in each box and a number ~M~, find the sum of all even snack counts and count how many boxes have at least ~M~ snacks.

### Input Specification
The first line will contain an integer ~N~ specifying how many groups of boxes need to be checked.
Each test case contains an integer ~B~, followed by ~B~ integers giving the snack counts in the boxes, followed by an integer ~M~.

### Output Specification
For each test case, output `Even total = X, Big boxes = Y`.

### Sample Input
    3
    5 5 8 11 12 8 10
    3 1 3 5 4
    4 20 20 19 2 20


### Sample Output
    Even total = 28, Big boxes = 2
    Even total = 0, Big boxes = 1
    Even total = 42, Big boxes = 2
