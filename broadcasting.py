op1 = np.array([i for i in range(9)]).reshape(3, 3)
op2 = np.array([[1, 2, 3]])
op3 = np.array([1, 2, 3])

# Notice that the results here are DIFFERENT!
print(op1 + op2)
print(op1 + op2.T)

# Notice that the results here are THE SAME!
print(op1 + op3)
print(op1 + op3.T)
