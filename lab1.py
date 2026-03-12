# 1
import numpy as np
arr = np.arange(10,51,5)
# print(arr)

# 2
zeros = np.zeros((4,6))
# print(zeros)   
zeros[2] = 99
# print(zeros)

# 3
arr = np.array([12,45,7,19,88,3,56,91,24,67])
# print(arr[arr > 50])

# 4
mat = np.eye(5)
mat[np.diag_indices(5)] = [10,20,30,40,50]
# print(mat)

# 5
x = np.arange(1,21).reshape(4,5)
# print(x)
print("-------")
# a 
# print(x[-2:, :])
#b
# print(x[:, 2:3])
# c
# print(x[:3, 2:])

# 6
a = np.array([1,2,3,4,5])
b= np.array([[10],
            [20],
            [30]])
# print(a+b)  # a stretches to be 3 rows and b stretches to be 5 columns

# 7
data = np.array([150,220,90,300,180,45])
normalized = (data - data.min()) / ( data.max() - data.min())
# print(normalized)

# 8
z_score = (data - data.mean()) / data.std()
# print(z_score)

# 9
mat = np.array([
    [4, 8, 1, 12],
    [7, 3, 9, 5],
    [11, 2, 6, 10],
    [15, 0, 14, 13]
])
# print(mat)
# print("-------")
# a
# print(mat.mean(axis=1, keepdims=True)) 
# b
# print(mat.sum(axis=0))  
# c
# print("Maximu value:", mat.max())
# print(np.unravel_index(mat.argmax(), mat.shape))

# 10
arr = np.arange(36).reshape(3,4,3) 
# print(arr)

# 11
arr = np.arange(1, 17).reshape(4,4)
# print(arr)
# print(arr.T)

# 12
ages = np.array([23, 45, 19, 34, 28, 51, 17, 39])
names = np.array(["Ali", "Sara", "Omar", "Lina", "Khaled", "Nour", "Yara", "Hassan"])
# print(names[(ages >= 25) & (ages <= 40)])

# 13
ages[ages < 20] = 20
# print(ages)

# 14
rand_mat = np.random.randint(1,101,(6,6))
# print(rand_mat)

np.random.seed(123)
rand_mat = np.random.randint(1,101,(6,6))
# print(rand_mat)

# 15
arr = np.random.normal(100,15,10)
# print(arr)

# 16
colors = ["red", "blue", "green", "yellow", "purple"]
rand_colors = np.random.choice(colors, size=3, replace=False)
# print(rand_colors)

# 17
nums = np.arange(1, 21)
np.random.shuffle(nums)  
# print(nums)
