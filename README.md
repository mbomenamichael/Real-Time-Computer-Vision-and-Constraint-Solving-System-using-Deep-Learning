Real-Time Computer Vision and Constraint Solving System using Deep Learning 

A real-time Sudoku solver that detects a Sudoku puzzle from a webcam feed, recognises digits using a Convolutional Neural Network (CNN), solves the puzzle algorithmically, and overlays the solution onto the video stream.

This project combines computer vision, deep learning, and algorithmic search to automatically interpret and solve Sudoku puzzles in real time.

![Sudoku Solver Demo](demo/demo.gif)

System Pipeline
Webcam Feed
     ↓
Sudoku Grid Detection (OpenCV)
     ↓
Perspective Transform
     ↓
Cell Segmentation (81 cells)
     ↓
Digit Recognition (CNN)
     ↓
Sudoku Solver (Backtracking)
     ↓
Solution Overlay on Video



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
