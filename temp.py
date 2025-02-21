import numpy as np
import matplotlib.pyplot as plt

# Define the datasets
data_25 = np.array([2, 5, 3, 7, 4, 3.5, 25])
data_neg3 = np.array([2, 5, 3, 7, 4, 3.5, -3])

# Sort the data
sorted_data_25 = np.sort(data_25)
sorted_data_neg3 = np.sort(data_neg3)

# Calculate median (u1)
u1_25 = np.median(sorted_data_25)
u1_neg3 = np.median(sorted_data_neg3)

# Calculate mean (u2)
u2_25 = np.mean(sorted_data_25)
u2_neg3 = np.mean(sorted_data_neg3)

# Printing results
print(f"For x = 25, Median (u1) = {u1_25}, Mean (u2) = {u2_25}")
print(f"For x = -3, Median (u1) = {u1_neg3}, Mean (u2) = {u2_neg3}")

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(12, 8))

# For x = 25
ax[0].plot(sorted_data_25, np.zeros_like(sorted_data_25), 'ro', label='Data Points')
ax[0].plot(u1_25, 0, 'go', label='Median (u1)')
ax[0].plot(u2_25, 0, 'bo', label='Mean (u2)')
ax[0].set_title('Dataset with x = 25')
ax[0].legend()

# For x = -3
ax[1].plot(sorted_data_neg3, np.zeros_like(sorted_data_neg3), 'ro', label='Data Points')
ax[1].plot(u1_neg3, 0, 'go', label='Median (u1)')
ax[1].plot(u2_neg3, 0, 'bo', label='Mean (u2)')
ax[1].set_title('Dataset with x = -3')
ax[1].legend()

plt.tight_layout()
plt.show()