
import matplotlib.pyplot as plt
 
#Plot a line graph
plt.plot([0.95412, 4.98547, 8.41411, 3.99, 10.9999], label='Rice')
plt.plot([3, 6], label='Oil')
plt.plot([8.0010, 14.2], label='Wheat')
plt.plot([1.95412, 6.98547, 5.41411, 5.99, 7.9999], label='Coffee')
 
# Add labels and title
plt.title("Interactive Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
 
plt.legend()
plt.show()