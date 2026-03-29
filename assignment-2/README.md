# Assignment 2

This folder contains the solutions for the 5 programming exercises of Assignment 2, written in Python 3.

## Execution Instructions

To run any of the programs, open your terminal and execute the corresponding command. For example:
`python3 fibonacci.py`

## Exercises Description

### 1. Fibonacci Numbers (`fibonacci.py`)
This program calculates the first *n* terms of the Fibonacci sequence and stores them in a list. The integer *n* is provided by the user. The numbers are calculated using the relation:
$F(n) = F(n-1) + F(n-2)$
with initial values $F(0) = 1$ and $F(1) = 1$.

### 2. List Input (`read_list.py`)
This program reads real numbers provided by the user and stores them in a list. The input process continues until the user enters the character `Q` to terminate it.

### 3. Pythagorean Triplets (`triplets_vers1` & `triplets_vers2`)
This program finds all integers $a, b, c$ that form a Pythagorean triplet ($a^2 + b^2 = c^2$) with the condition that their sum (perimeter) does not exceed a user-defined limit $p$ ($a + b + c \le p$). Each valid triplet is stored as a tuple inside a list. 

**Note:** This file includes two distinct algorithmic approaches for solving the problem:
* **1st Method:** An exhaustive search algorithm with a time complexity of $O(p^3)$.
* **2nd Method:** An optimized algorithm with a time complexity of $O(p^2)$, which utilizes the mathematical properties of the triplets to minimize iterations.

### 4. Merging 2 Lists (`merge_lists.py`)
This program generates two lists, $L1$ and $L2$, containing $n1$ and $n2$ random natural numbers respectively. The numbers do not exceed a user-defined maximum value $M$. It then merges the elements of both lists into a new list $X$ in ascending order. The built-in sorting methods of Python are only used for $L1$ and $L2$, while the merging logic for $X$ is manually implemented.

### 5. Unique List Merge (`unique_merge_lists.py`)
This is a modification of the previous program. It merges the two generated lists ($L1$ and $L2$) into a new sorted list $X$, but ensuring that the final merged list contains absolutely no duplicate elements.
