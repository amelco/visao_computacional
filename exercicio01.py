import numpy as np

# Questão 1
A = np.random.randint(0, 10, size=(3,4))

# Questão 2
B = np.random.randint(0, 10, size=(3,4))

# Questão 3
A = np.clip(A, 1, 4)
B = np.clip(A, 1, 4)

# Questão 4
print(f"A tipo: {A.dtype}\nA dims: {A.shape}")

# Questão 5
C = np.full((3, 4), 2)

# Questão 6
D = np.add(A, np.multiply(2,B))

# Questão 7
E = np.array([[2],[3],[4],[5]])

# Questão 8
F = np.dot(B, E)

# Questão 9
G = np.copy(F)

# Questão 1#0
A_sum = A.sum()

# Questão 11
A = A.astype('float64')

# Questão 12
A = np.transpose(A)

# Questão 13
A_vec = A.flatten()

# Questão 14
new_row = [1, 1, 1]
A = np.vstack([A, new_row])

# Questão 15
v = np.linspace(0, 1, 5)
