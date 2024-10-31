# %% [markdown]
# # Numpy

# %%
# %pip install numpy

# %%
import numpy as np

# %%
print(np.array([1, 2, 3, 4]))

# %%
a = np.array([
    [1, 2, 3], 
    [1, 2, 3]
])
b = np.array([[1, 2, 2], [1, 2, 2], [1, 4, 5]])
c = np.array([
    [1, 2], [2, 3]
])

# %%
a.dot(b)
# a.dot(c) # error

# %%
a * a

# %%
a @ b

# %%
x = np.array([2 ,4 ,5, 6, 10, 11])

x.shape

# %%
x[4:6]
x[0]
x[-1]
x[1:4:1]
x[2:-1:2]

# %%
np.sum(x)
np.mean(x)

# %%
y = np.arange(0, 12)
y

# %%
y.reshape(2, 6)

# %%
np.zeros(shape=(8, 8))

# %%
np.ones(shape=(4, 4))

# %%
np.repeat(2, 5)

# %%
np.full(shape=(2, 3), fill_value=2)

# %%
b = np.full(shape=(8, 8), fill_value="b")
b[1::2, ::2] = "w"
b[::2, 1::2] = "w"
b

# %%
np.random.seed(0)
np.random.randint(2, 5, size=(2, 3))

# %%
np.random.choice([3, 2, 5, 6], p=[0.1, 0.2, 0.2, 0.5], size=(2, 3))

# %%
a.T

# %%
np.delete(a, 0, axis=1)

# %%
x = np.random.randint(1, 50, size=20)

# %%
x[x < 5]

# %%
x[(x < 15) & (x > 10)]
# x[10 < x < 15] # error

# %%
x[(x > 10) | (x < 5)].shape

# %%
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

# %%
np.stack([a, b], axis=1)

# %%
np.stack([a, b], axis=0)

# %%
np.concatenate([a, b], axis=0)
