## The Moon Gate Password

At the Moon Gate, an ancient owl asks each traveler for a password phrase. The gate ignores spaces and capital letters, then checks whether the phrase reads the same forward and backward. A true moon password opens the gate.

## Your Task 
Given a phrase containing letters and spaces, ignore all spaces and compare letters without caring about uppercase or lowercase. Output TRUE if the cleaned phrase is a palindrome, otherwise output FALSE.

### Input Specification
The first line will contain an integer ~N~ (~1 \le N \le 100\,000~) specifying how many passwords owl has to check 
The next ~N~ lines will each contain the phrase that needs to be verified.

### Output Specification
Output either TRUE or FALSE in all capital letters and without any spaces or quotes.

### Sample Input
    3
    never odd or even
    moon gate
    Was it a cat I saw


### Sample Output
    TRUE
    FALSE
    TRUE
