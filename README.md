![Python](https://img.shields.io/badge/Python-3.9-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
# Real-Time Sudoku Solver

A real-time Sudoku solver that detects a Sudoku grid from a live camera feed, recognises the digits using a **Convolutional Neural Network (CNN)**, solves the puzzle using a **backtracking algorithm**, and overlays the solution on the video stream.

The system combines **computer vision**, **machine learning**, and **algorithmic problem solving** to automatically interpret and solve Sudoku puzzles in real time.

![Sudoku Solver Demo](demo/demo.gif)
---

## Features

- Real-time Sudoku grid detection using **OpenCV**
- Digit recognition with a **CNN built using TensorFlow/Keras**
- Automatic Sudoku solving using a **backtracking algorithm**
- Live overlay of the solved digits onto the detected grid
- Performance metrics including **FPS and solve time**

## Tech Stack

### Languages & Libraries

- Python
- OpenCV
- TensorFlow / Keras
- NumPy / SciPy

### Concepts Used

- Convolutional Neural Networks (CNNs)
- Image preprocessing & thresholding
- Perspective transformation
- Contour detection
- Backtracking search algorithms

## Project Structure

```text
.
├── sudoku5.py                # Main real-time Sudoku solver script
├── sudoku_solver.py          # Backtracking Sudoku solving algorithm
├── numberrecognitionmodel.py # CNN training script for digit recognition
├── NumberRecognition.h5      # Trained digit recognition model
├── RealTimeSudokuSolver.pdf  # Project report
```
## Why This Project Matters

This project demonstrates an end-to-end **AI pipeline** combining:

- Computer vision for grid detection  
- Deep learning for digit recognition  
- Classical algorithms for constraint solving  
- Real-time system integration  

It highlights how **machine learning models can be integrated into complete applications**, rather than used in isolation.

## How It Works

1. Capture frames from a webcam.  
2. Detect the Sudoku grid using contour detection and perspective transformation.  
3. Split the grid into **81 cells**.  
4. Use a **CNN model** to recognise digits in each cell.  
5. Convert the grid into a digital Sudoku board.  
6. Solve the puzzle using a **backtracking algorithm**.  
7. Overlay the solved digits onto the original video frame.

## Running the Project

Install dependencies:

```bash
pip install opencv-python tensorflow keras numpy scipy
python sudoku5.py
```

## Results

- ~24 FPS real-time performance  
- ~2–3 seconds to solve a puzzle after recognition  
- ~92% digit recognition accuracy  
- ~98% Sudoku solving success rate under normal conditions  

---

## Future Improvements

- Improve digit recognition accuracy with larger datasets  
- Handle skewed or rotated Sudoku boards  
- Improve robustness to lighting conditions  
- Extend solver to larger puzzles (e.g., **16×16 Sudoku**)  












System Pipeline

```
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
```

## Author

Michael Mbomena  
MSc Artificial Intelligence  
GitHub: https://github.com/mbomenamichael


