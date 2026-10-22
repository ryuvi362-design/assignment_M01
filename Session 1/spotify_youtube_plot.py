import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

spotify = [2, 3, 1, 4, 2, 3, 5]

youtube = [1, 2, 3, 2, 4, 3, 2]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(days, spotify, marker="o", color="green")
axes[0].set_title("Spotify Listening Hours")
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Hours")
axes[0].grid(True)

axes[1].plot(days, youtube, marker="o", color="red")
axes[1].set_title("YouTube Viewing Hours")
axes[1].set_xlabel("Days")
axes[1].set_ylabel("Hours")
axes[1].grid(True)

plt.tight_layout()

plt.show()