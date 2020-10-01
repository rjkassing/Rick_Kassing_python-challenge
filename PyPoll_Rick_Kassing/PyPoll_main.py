import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('PyPoll_Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    total_votes=0

    # Create a dictionary to hold the candidates names.
    candidates = {}
    max_votes = 0
    winner = ""
    list2 = []
    #candidates = []
    candidate = {}    
    # Create a dictionary using the built-in function.
    candidates = dict()

    # Total Number of Votes Cast
    for row in csvreader:
        total_votes=total_votes+1
    #Find the number of unique candiates
        if row[2] not in list2:
           #List of unique candidates in row2 
            list2.append(row[2])
            candidates[row[2]] = 0
            #If candidate is not unite, add vote to thier count        
        candidates[row[2]] = candidates[row[2]]+1
    # Calaculate the number of votes/candidate
        percent_dict = {}
    # Calaculate the % of votes/candidate
    for x in candidates:
        percent_dict[x] = ((candidates[x] / total_votes) * 100)
        votes = candidates.get(x)
        if votes > max_votes:
             max_votes = votes
             winner = x

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {(total_votes)}")
print(f"-------------------------")
for x in candidates:
    print(str(x), round(percent_dict[x],5), (candidates[x]))
print(f"-------------------------")
print(f"Winner : {(winner)}")
print(f"-------------------------")

Final_Results= open('Final_Results.txt', 'w')

# Write the lines for the text file
Final_Results.write(f"Election Results" + "\n")
Final_Results.write("-------------------------" + "\n")
Final_Results.write("Total Votes: {(total_votes)}" + "\n")
Final_Results.write("-------------------------" + "\n")
Final_Results.write("-------------------------" + "\n")
Final_Results.write("Winner : {(winner)}" + "\n")
Final_Results.write("-------------------------" + "\n")