# Assignment 1

This folder contains the solutions for the 4 programming exercises of Assignment 1, written in Python 3.

## Execution Instructions

To run any of the programs, open your terminal and execute the corresponding command.

## Exercises Description

### 1. Roots of a quadratic equation (`polynomial.py`)
This program asks the user for the coefficients of a 2nd-degree polynomial and calculates its real roots (if they exist).

### 2. Base of natural logarithms (`epsilon.py`)
This program approximates the value of the mathematical constant *e* with a given precision *δ* provided by the user. The value of *e* is approximated using the series expansion:

e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n! + ...

The algorithm terminates when *δ* becomes smaller than the approximation error with *n* terms, meaning:
δ ≤ 3 / (n + 1)!

To optimize calculations and avoid redundant multiplications, the property `(n + 1)! = n!(n + 1)` is used.

### 3. Number of digits (`million.py`)
This program calculates the smallest positive integer whose factorial has at least 1,000,000 digits. The calculation is based on the sum of logarithms:

log10(n!) = log10(2) + log10(3) + ... + log10(n)

The number of digits of a positive integer *x* is calculated using the formula: `math.floor(math.log10(x)) + 1`.

### 4. Character patterns (`stars.py`)
This program displays a diagonal pattern of asterisks on the screen. The number of asterisks on the diagonal (*n*) is given as input by the user.
