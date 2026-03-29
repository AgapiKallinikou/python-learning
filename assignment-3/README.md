# Assignment 3

This folder contains the Python solutions for the exercises of Assignment 3, focusing on matrix operations, custom data processing, interval discretization, and computational geometry using both recursive and iterative approaches.

---

## File Structure & Recommended Naming

To keep the project organized, the following filenames are used:
* **`matvec.py`**: Matrix-vector multiplication logic.
* **`foo_function.py`**: Manual calculation of sum, max, and indices (Exercise 2).
* **`linspace.py`**: Interval discretization mimicking MATLAB's behavior.
* **`polygon_area.py` & `poly_area2`**: Area calculation of convex polygons (both Recursive and Iterative).

---

## Exercises Description

### 1. Matrix-Vector Multiplication (`matvec.py`)
This program implements a function `matvec(A, x)` where matrices and vectors are represented as 2D and 1D lists, respectively. 
* **Functionality**: Returns the product of matrix $A$ and vector $x$.
* **Error Handling**: If dimensions are incompatible, the function returns an empty list `[]`.

### 2. Tuple List Processing (`foo_function.py`)
A specialized function (based on a past exam question) that processes a list of tuples containing integers. Without using built-in functions like `sum()`, `max()`, or `index()`, it calculates:
* The **sum** of elements in each tuple.
* The **maximum** element.
* The **index** of the first occurrence of the maximum element.
The results are returned as a list of tuples containing these three values.

### 3. The `linspace` Function (`linspace.py`)
Replicates the functionality of MATLAB's `linspace(a, b, n)`.
* **Logic**: Divides the interval $[a, b]$ into $n$ equally spaced points, including the endpoints.
* **Default Behavior**: If $n$ is not provided, it defaults to **100** points.

### 4 & 5. Convex Polygon Area (`polygon_area.py` & `poly_area2.py`)
These exercises calculate the area of a convex polygon defined by a list of vertex coordinates $(x_k, y_k)$. The area is calculated by decomposing the polygon into triangles using the formula:

$$\text{Area} = \frac{|x_Ay_B - x_Ay_C + x_By_C - x_By_A + x_Cy_A - x_Cy_B|}{2}$$

**Implementation Approaches:**
* **Recursive Method (`polygon_area`)**: Solves the problem by recursively breaking the polygon into smaller triangular sections.
* **Iterative Method (`poly_area2`)**: Solves the same problem using a `for` loop, which is more efficient for polygons with a high number of vertices as it avoids recursion depth limits.

*Note: Both methods utilize a helper function `tri_area` to perform the triangle calculations.*

---

## Execution Instructions
To run any of the scripts, ensure you have Python 3 installed and execute via terminal.
