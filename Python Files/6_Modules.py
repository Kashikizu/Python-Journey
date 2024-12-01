import matplotlib.pyplot as plt

x = [i for i in range(-10, 11)]
y = [(i**2 - i) for i in x]

print(x, y)

plt.plot(x, y)

plt.show()