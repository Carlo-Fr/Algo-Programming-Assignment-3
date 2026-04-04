# Algo-Programming-Assignment-3

# Highest Value Longest Common Sequence (HVLCS)

## Team Members
* Carlo Fraley - UFID: [Your UFID]
* Kavi Patel - UFID: [Partner UFID]

## Execution Instructions
* **Prerequisites:** Python 3
* **Run:** `python src/hvlcs.py < data/example.in`

## Assumptions
* Input files will follow the format order of alphabet size, character value mappings, then the two strings.

## Written Component

### Question 1: Empirical Comparison
* 

### Question 2: Recurrence Equation
* **Recurrence:** Let $M[i][j]$ represent the maximum value of a common subsequence between the prefix of string A (length $i$) and the prefix of string B (length $j$), with $v(A[i])$ being the value of the character.
  
  $$M[i][j] = M[i-1][j-1] + v(A[i]) \quad \text{if } A[i] = B[j]$$
  
  $$M[i][j] = \max(M[i-1][j], M[i][j-1]) \quad \text{if } A[i] \neq B[j]$$

* **Base Cases:** $M[i][0] = 0$ and $M[0][j] = 0$ for all i and j. 
  This occurs because comparing any string against an empty string yields a common subsequence of length zero, which has a total value of zero, and we account for this for both i and j.

* **Correctness:** When characters match, adding the character's value to the previous optimal state guarantees the maximum running total. This reflects the part where we add the character's value and then move the index down by one for both i and j. When characters mismatch, we want to carry forward the maximum value from whichever preceding prefix path is best, which is why we check the max for moving down the index in either the A string or the B string.

### Question 3: Big-Oh
* 