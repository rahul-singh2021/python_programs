#Python Programs Repository

Welcome to the Python Programs Repository! This repository is dedicated to showcasing a collection of Python programs, designed to demonstrate various concepts, algorithms, and applications using the Python programming language.

The goal of this repository is to provide a valuable resource for both beginners and experienced Python developers alike. Whether you are just starting your coding journey or looking to enhance your skills, you will find a wide range of programs that cover different topics and areas of interest.


# 1:pie chart program

This is a simple Python program that demonstrates the use of stack plots using Matplotlib library. It shows the distribution of activities (sleeping, eating, working, and playing) over a period of five days.

## Requirements

- Python 3.x
- Matplotlib library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahul-singh2021/python_programs.git

## output

  ![image](https://github.com/rahul-singh2021/python_programs/assets/95570957/969cad7c-4f90-4620-bec3-371243acd816)


# 2:area graph Program

This program uses the `matplotlib` library to create a stack plot, visualizing the distribution of time spent on different activities over five days.

## Dependencies

- Python 3.x
- `matplotlib` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahul-singh2021/python_programs.git
   
##  output

   ![image](https://github.com/rahul-singh2021/python_programs/assets/95570957/754150a4-66fd-4710-9c45-8404994f0a22)

# 3:bar graph Program

This program uses the `matplotlib` library to create a stack plot, visualizing the distribution of time spent on different activities over five days.

## Dependencies

- Python 3.x
- `matplotlib` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahul-singh2021/python_programs.git
   
 ## output 

![image](https://github.com/rahul-singh2021/python_programs/assets/95570957/80588691-b64e-4a07-a68c-23c0e6029120)

# 4:sin and cosine grapg Program

This repository contains a Python script that generates a plot of the sine and cosine functions using the NumPy and Matplotlib libraries.

## Dependencies

- Python 3.x
- `matplotlib` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahul-singh2021/python_programs.git
   
 ## output 
![image](https://github.com/rahul-singh2021/python_programs/assets/95570957/dd960e04-3531-42a7-8ab3-fda51ffeef46)


# 5:Matrix Multiplication Program

This program demonstrates matrix multiplication using NumPy.

## Description

This program performs matrix multiplication on two matrices, `matrix1` and `matrix2`, using the `numpy.matmul()` function. The resulting matrix is stored in the variable `multiplication`.

## Usage

1. Install the required dependencies: Make sure you have NumPy installed. You can install it using pip:


# 6:Binary Search Tree

This program demonstrates the implementation of a Binary Search Tree (BST) in Python.

## Program Description

The program defines a `Node` class representing a node in the BST. Each node has a `data` value and references to its left and right children. The class provides methods to insert nodes into the tree and print the tree in order.

The `insert` method allows inserting nodes into the BST by comparing the data value with the current node's data. If the value is less, the method recursively traverses to the left child and inserts the node there. If the value is greater, the method traverses to the right child.

The `PrintTree` method uses inorder traversal to print the nodes of the tree in ascending order.

## Usage

- Create a `Node` object to represent the root of the tree.
- Use the `insert` method to add nodes to the tree, passing the data value to be inserted.
- Call the `PrintTree` method to print the elements of the tree in order.


 ## Example


 root = Node(12)
 root.insert(6)
 root.insert(14)
 root.insert(3)
 root.PrintTree()
 ##Output:
   3
   6
   12
   14




## 7: broadcasting

## Introduction
This program demonstrates the usage of NumPy arrays and showcases various operations performed on them.

## Code Explanation
The code snippet provided demonstrates the usage of NumPy arrays to perform element-wise addition between arrays `op1`, `op2`, and `op3`. It showcases the difference between adding a 1D array to a 2D array and transposing the 1D array to a column vector before performing addition.

## Usage
To run this program, you need to have Python and the NumPy library installed. You can install NumPy using pip:
   
##otput 
  [[ 1  3  5]
  [ 4  6  8]
  [ 7  9 11]]
 [[ 1  2  3]
  [ 5  6  7]
  [ 9 10 11]]
 [[ 1  3  5]
  [ 4  6  8]
  [ 7  9 11]]
 [[ 1  3  5]
  [ 4  6  8]
  [ 7  9 11]]


# 8:Peak Point Finder

This Python program finds the peak point in an array using a binary search algorithm.

## Requirements

- Python 3.x
- NumPy

## Installation

1. Clone the repository or download the source code files.

```shell
git clone https://github.com/rahul-singh21/python_programs.git


# 9:Binary Search Program

This program implements the binary search algorithm to find the index of a given number in a sorted array.

## Usage

To use this program, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone or download the repository containing the program.
3. Open the terminal or command prompt and navigate to the directory where the program is located.
4. Run the program using the command: `python binary_search.py`.

## Algorithm

The binary search algorithm works as follows:

1. Initialize two variables, `f` and `l`, as the first and last indices of the array, respectively.
2. While `f` is less than or equal to `l`:
   - Calculate the middle index, `mid`, as the average of `f` and `l`.
   - If the target number `x` is less than the element at `mid`, update `l` to `mid - 1`.
   - If the target number `x` is greater than the element at `mid`, update `f` to `mid + 1`.
   - If the target number `x` is equal to the element at `mid`, return `mid`.
3. If the target number is not found in the array, return -1.

## Example

Consider the following example:

```python
array = np.array([6, 3, 1, 7, 2, 10, 5, 37, 8])
array = sorted(array)

x = 8

index = binarysearch(array, x)

print("The given number is located at:", index)
