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

array = np.array([6, 3, 1, 7, 2, 10, 5, 37, 8])
array = sorted(array)

x = 8

index = binarysearch(array, x)

print("The given number is located at:", index)


# 10:Armstrong Number Checker

This Python program checks whether a given number is an Armstrong number or not.

## Description

An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

The program takes a number as input and calculates the sum of its digits raised to the power of 3. It then compares the result with the original number to determine if it is an Armstrong number or not. The program provides the output accordingly.

## Usage

1. Run the program.
2. Enter a number when prompted.
3. The program will calculate the sum of the digits raised to the power of 3 and compare it with the original number.
4. It will then display whether the number is an Armstrong number or not.

# 11:Heap Sort
This is a Python program that demonstrates the implementation of Heap Sort algorithm. Heap Sort is a comparison-based sorting algorithm that utilizes a binary heap data structure to sort elements efficiently.

## Program Description
The program uses the heappop and heappush functions from the heapq module, which provide the necessary operations to maintain a min-heap. The heapsort function takes a list of elements as input and sorts them in ascending order using the heap data structure.

## The steps performed by the program are as follows:

Create an empty heap.
Iterate over each element in the input list and insert it into the heap using the heappush function.
Create an empty list called sort.
While the heap is not empty, repeatedly remove the smallest element from the heap using the heappop function and append it to the sort list.
Return the sort list, which contains the sorted elements.
## Usage
To use this program, follow these steps:

Ensure you have Python installed on your system.
Copy the code into a Python file or clone the repository.
Import the heappop and heappush functions from the heapq module.
Call the heapsort function, passing a list of elements as an argument.
The function will return a new list with the elements sorted in ascending order.
Print the sorted list or use it as needed in your application.


# 12:Angle Calculation
This is a Python program that calculates the angle between two sides of a right-angled triangle. The program uses the atan function from the math module to calculate the angle in radians, and then converts it to degrees using the deg function.

## Program Description
The program defines a function called solve that takes two arguments: ab (length of the side opposite to the angle) and bc (length of the side adjacent to the angle). The function calculates the angle using the formula atan(ab/bc), where atan is the arctangent function. The deg function is defined inside solve and is used to convert the angle from radians to degrees.

## The steps performed by the program are as follows:

Import the atan function from the math module.
Define the deg function that takes an angle in radians and converts it to degrees by multiplying it with 180/pi, where pi is the mathematical constant.
Define the solve function that takes ab and bc as arguments.
Calculate the angle in radians using the formula atan(ab/bc) and store it in the variable ans.
Convert the angle from radians to degrees by calling the deg function on ans.
Return the calculated angle in degrees.
Set the values of ab and bc to the desired lengths.
Call the solve function with ab and bc as arguments.
Print the calculated angle.

# 13: Scatter Plot

This repository contains code for creating a scatter plot using machine learning with numpy and matplotlib.

## Prerequisites

- Python 3
- Numpy
- Matplotlib

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/rahul-singh21/python _programs.git

## output
    
  ![image](https://github.com/rahul-singh2021/python_programs/assets/95570957/e1cc568a-8513-413b-aabc-1224319f4950)

# 14:Largest Number Finder

This Python program finds the largest number among three input numbers.

## Usage

1. Modify the values of `num1`, `num2`, and `num3` variables in the program to change the input numbers.
2. Uncomment the following lines if you want to take three numbers from the user as input.
   ```python
   #num1 = float(input("Enter first number: "))
   #num2 = float(input("Enter second number: "))
   #num3 = float(input("Enter third number: "))
   
   
# 15:Armstrong Number Checker

This Python program checks for Armstrong numbers within a specified interval.

## How it works

The program iterates over a given range of numbers and checks if each number is an Armstrong number.

An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits it has. For example, 153 is an Armstrong number because:

1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

The program calculates the order of each number (number of digits) using `len(str(num))`. Then, it initializes a sum variable and iterates through each digit of the number, raising it to the power of the order and adding it to the sum. If the sum equals the original number, it is an Armstrong number, and it is printed.

## Usage

To use this program, simply specify the desired range of numbers by modifying the `lower` and `upper` variables in the code. Then, run the program, and the Armstrong numbers within that range will be printed to the console.

      ```python
      lower = 100
      upper = 2000
      
      for num in range(lower, upper + 1):
          # order of number
          order = len(str(num))
          
          # initialize sum
          sum = 0
      
          temp = num
          while temp > 0:
              digit = temp % 10
              sum += digit ** order
              temp //= 10
      
          if num == sum:
              print(num)   


# 16:Circular Linked List Example

This is an example program that demonstrates the implementation of a circular linked list in Python.

## Program Description

The program defines two classes: `Node` and `circularLinkedList`.

### `Node` Class

The `Node` class represents a node in the circular linked list

# 17:Stack Program

   This program demonstrates the implementation of a stack using a list in Python.

## Usage

   1. Run the program `stack.py` in a Python environment.
   2. The program initializes an empty stack.
   3. Elements 'a', 'b', and 'c' are pushed onto the stack using the `append()` function.
   4. The program then demonstrates the LIFO (Last-In-First-Out) behavior of the stack by popping the elements using the `pop()` 
      function.
   5. The popped elements are displayed on the console.
   6. Finally, the program shows the stack's contents after the elements are popped.

## How to Run

   Make sure you have Python installed on your system. Then, follow these steps:

   1. Clone the repository:
      git clone https://github.com/rahul-singh21/python_programs.git

# 18:Graph Implementation

         This program demonstrates the implementation of a graph using dictionaries in Python.

## Functionality

   - `add_vertex(v)`: Add a vertex to the graph.
   - `add_edge(v1, v2, e)`: Add an edge between two vertices with a specified edge weight.
   - `print_graph()`: Print the graph and its edges.

## Usage

   1. Add vertices to the graph using `add_vertex(v)`.
   2. Add edges between the vertices using `add_edge(v1, v2, e)`.
   3. Print the graph using `print_graph()`.

## Example

   # Create the graph
   graph = {}
   vertices_no = 0
   add_vertex(1)
   add_vertex(2)
   add_vertex(3)
   add_vertex(4)

   # Add edges between vertices
   add_edge(1, 2, 1)
   add_edge(1, 3, 1)
   add_edge(2, 3, 3)
   add_edge(3, 4, 4)
   add_edge(4, 1, 5)

   # Print the graph
   print_graph()

   # Internal representation
   print("Internal representation: ", graph)

# 19:Doubly Linked List

   This is a Python implementation of a doubly linked list. It consists of two classes: `Node` and `DoublyLinkedList`.

## Node Class

   The `Node` class represents a single node in the doubly linked list. It has the following attributes:

   - `data`: Holds the data stored in the node.
   - `next`: Points to the next node in the list.
   - `prev`: Points to the previous node in the list.

## DoublyLinkedList Class

   The `DoublyLinkedList` class represents the doubly linked list. It has the following attributes:

   - `head`: Points to the first node in the list.
   - `tail`: Points to the last node in the list.

### Methods

   - `push_front(new_data)`: Adds a new element at the beginning of the list.
   - `push_back(new_data)`: Adds a new element at the end of the list.
   - `peek_front()`: Returns the value of the first element without removing it.
   - `peek_back()`: Returns the value of the last element without removing it.
   - `pop_front()`: Removes and returns the first element.
   - `pop_back()`: Removes and returns the last element.
   - `insert_after(temp_node, new_data)`: Inserts a new node after a given node.
   - `insert_before(temp_node, new_data)`: Inserts a new node before a given node.

Feel free to use and modify this implementation for your own needs.


# 20:Fibonacci Number Checker

   This Python program checks whether a given number is a Fibonacci number.

## Usage

   1. Make sure you have Python installed on your machine.
   2. Clone or download the repository containing the program.
   3. Open a terminal or command prompt and navigate to the directory where the program is located.
   4. Run the program by executing the following command:
      
         ```shell
         python fibonacci_check.py

# 21:Matrix Multiplication Program

   This is a Python program that performs matrix multiplication using nested loops.

## Description

   The program multiplies two matrices, `A` and `B`, and stores the result in `result`. It utilizes nested loops to iterate over the 
   rows and columns of the matrices. The resulting matrix is then printed.

## Usage

   1. Modify the matrices `A` and `B` in the code according to your requirements.
   2. Run the program to execute the matrix multiplication.
   3. The resulting matrix will be displayed in the console.
   4. 


# 22:Matrix Transpose Program

   This program transposes a given matrix using a nested loop. It takes a matrix `X` as input and generates the transpose matrix 
   `result`. The transpose of a matrix is obtained by interchanging its rows with columns.

## Usage

   - Modify the matrix `X` in the program if you want to transpose a different matrix.
   - Run the program and observe the output.   

    git clone https://github.com/rahul-singh21/python_programs.git
