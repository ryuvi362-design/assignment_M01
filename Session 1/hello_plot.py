import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

steps = [3000, 4500, 5000, 4000, 6500, 7000, 8000]

plt.plot(days, steps, marker="o")

plt.xlabel("Days")
plt.ylabel("Number of Steps")
plt.title("Daily Steps Walked in 7 Days")

plt.show()