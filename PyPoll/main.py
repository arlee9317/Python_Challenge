# Import modules
import os
import csv
import pandas as pd
import numpy as np

csvpath = os.path.join("Resources", "election_data.csv")

Total_Votes = []
Khan_Count = 0
Correy_Count = 0
Li_Count = 0
Tooley_Count = 0
percent = "%"


with open(csvpath) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #loop through to count the number of election results for each candidate
    for row in csv_reader:

    	Total_Votes.append(row[0])

    	if row[2] == "Khan":
    		Khan_Count = Khan_Count + 1
    	elif row[2] == "Correy":
    		Correy_Count = Correy_Count + 1
    	elif row[2] == "Li":
    		Li_Count = Li_Count + 1
    	else:
    		Tooley_Count = Tooley_Count +1

#Find percentage of votes for each candidate 
Perc_Khan = (Khan_Count/len(Total_Votes)) * 100
Perc_Correy = (Correy_Count/len(Total_Votes)) * 100
Perc_Li = (Li_Count/len(Total_Votes)) * 100
Perc_Tooley = (Tooley_Count/len(Total_Votes)) * 100

Election_Results = pd.DataFrame({
    "Candidate": ["Khan", "Correy", "Li", "O'Tooley"],
    "Voter_Percentage": [Perc_Khan, Perc_Correy, Perc_Li, Perc_Tooley]})

#Print out results
print("Election Results")
print("------------------------")
print("Total Votes" + " " + str(len(Total_Votes)))
print("------------------------")
print(f"Khan: {round(Perc_Khan)}% ({Khan_Count})")
print(f"Corey: {round(Perc_Correy)}% ({Correy_Count})") 
print(f"Li: {round(Perc_Li)}% ({Li_Count})")
print(f"O'Tooley: {round(Perc_Tooley)}% ({Tooley_Count})")
print("------------------------")
print("Winner:"+ " " + Election_Results.loc[Election_Results["Voter_Percentage"].idxmax(), "Candidate"])
print("------------------------")

#output text file
np.savetxt("Results.txt", Election_Results.values, fmt = "%s,%d", delimiter =",", header="Candidate, Voter_Percentage")
