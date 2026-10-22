import matplotlib.pyplot as plt

posts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

likes = [120, 180, 150, 230, 300, 270, 350, 400, 380, 450]

plt.plot(posts, likes, marker="o", color="purple")

plt.xlabel("Instagram Posts")
plt.ylabel("Number of Likes")

plt.title("Likes on Last 10 Instagram Posts")

plt.show()