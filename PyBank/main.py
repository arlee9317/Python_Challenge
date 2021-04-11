#import modules
import pandas as pd 
import csv
import os

path = os.path.join("Analysis", "PyBank_data.txt")

#find path for data you are trying to read from
file = ("Resources/budget_data.csv")

#read pandas to read file
df = pd.read_csv(file)
df.columns

#Getting row count for just the Date column 
Total_months = df.set_index(['Date'])
#print(len(Total_months))

# Summing the total profit/Losses
Total_PF = df["Profit/Losses"].sum()
#print(Total_PF)

#Get values from the Profit/Losses and create a list

Average = []
x = 0
amount = 0

for items, row in df.iterrows():
    
    try:
        x = row["Profit/Losses"]
        Average.append(x)
   
    except IndexError:
        continue 

#Error checking with print statement
#print(Average) 

# loop through this list to find the change from row i to row i + 1
change = []
i = 0

for i in range(len(Average)):
    try:
        y = (Average[i] - Average[i+1])
        change.append(y)
    
    except IndexError:
        y = Average[i]

#Error checking
#print(change)

#sum all the changes in the array
Sum_change = int(sum(change)/len(Average))
print(Sum_change)

# error checking max/min of the changes
#print(max(change))
#print(min(change))

#Text_write = {"Total Months":len(Total_months), "Total": Total_PF, "Average Change": Sum_change, "Greatest Increase in Profits:": max(change), "Greatest Decrease in Profits:": min(change)}


print("Finacial Analysis")
print("-------------------------")
print(f"Total Months: {len(Total_months)}")
print(f"Total: ${Total_PF}")
print(f"Average Change: ${Sum_change}")
print(f"Greatest Increase in Profits: ${max(change)}")
print(f"Greatest Decrease in Profits: ${min(change)}")



#write text file

with open(path, "w") as File1:
	File1.write(f"Total Months: {len(Total_months)}\n")
	#File.write("\n") #New line
	File1.write(f"Total: ${Total_PF}\n")
	#File.write("\n") #New line
	File1.write(f"Average Change: ${Sum_change}\n")
	#File.write("\n") #New line
	File1.write(f"Greatest Increase In Profits: (${max(change)}) \n")
	#File.write("\n") #New line
	File1.write(f"Greatest Decrease In Profits: (${min(change)}) \n")
	File1.close()