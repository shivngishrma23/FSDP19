
import pandas as pd

# Reading CSV file
dataset = pd.read_csv('Automobile.csv')

# Replacing the blank space with nan (Not a Number)
dataset["price"][dataset["price"] == '  '] = 'nan'

# Converting the datatype of price column from object to flaot
dataset["price"] = dataset["price"].astype(float)

# Filling the missing values with average of price column
dataset["price"] = dataset["price"].fillna(dataset["price"].mean())

# Converting the price column into a numpy.ndarray
price_numpy_array = dataset["price"].values

print ( "Minimum Price is {0}".format( dataset["price"].min() ) )
print ( "Maximum Price is {0}".format( dataset["price"].max() ) )
print ( "Average Price is {0}".format( round( dataset["price"].mean(), 2 ) ) )
print ( "Standard Deviation of Price is {0}".format( round( dataset["price"].std(), 2 ) ) )