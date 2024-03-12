import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Task3_data.csv")
#print(data)
#user types in destination and date and then use pandas to create a dataset with that condition
Destination = input("Type in your destination: ")
date = input("Type in the date: ")
SortedData = data[(data["Desination"] == Destination) & (data["Month"])]
print(SortedData)
# group the data via airline and work out the mean price
average_price = SortedData.groupby("Airline")["Price"].mean()
#makes matplotlib easier to read
average_price_df = average_price.reset_index()

# generate a graph of that dataset using matplotlib
plt.bar(average_price_df["Airline"], average_price_df["Price"])
plt.title("Bar chart for Airline")
plt.xlabel("Airline")
plt.ylabel("Price")
plt.show()



