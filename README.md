How the System Works
1. Grid Detection

The webcam feed is processed using Gaussian blur and adaptive thresholding to detect contours and locate the Sudoku grid.

2. Perspective Transformation

The detected grid is warped into a square using a perspective transform to standardise the puzzle layout.

3. Digit Recognition

Each cell is resized to 28×28 grayscale and passed to a CNN classifier trained to recognise digits.

4. Sudoku Solving

The detected puzzle is solved using a constraint-based backtracking algorithm implemented in Python.

5. Solution Overlay

The solved digits are projected back onto the original camera frame in real time.
