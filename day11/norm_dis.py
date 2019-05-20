import numpy as np
incomes = np.random.normal(150, 20, 1000)
print(incomes)


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

plt.hist(incomes,100)
plt.show()

sd = print("Standard Deviation is: ", np.std(incomes))
v = sd*sd 
print(v)