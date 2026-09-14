import matplotlib.pyplot as plt

marks = [23, 33, 23, 12, 65, 87, 34, 66, 77, 13]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")

plt.show()