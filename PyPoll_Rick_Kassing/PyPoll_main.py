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
    winner = {}
    list2 = []
# Create a dictionary using the built-in function.
    candidates = dict()

    # Total Number of Votes Cast
    for row in csvreader:
        total_votes=total_votes+1
        if row[2] not in list2:
            list2.append(row[2])
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]]+1

        percent_dict = {}
    for x in candidate_dict:
        percent_dict[x] = round((candidate_dict[x] / total_votes) * 100, 2)
        votes = candidate_dict.get(x)
        if votes > max_votes:
             max_votes = votes
             winner = x
output = f"{x} : {percent_dict[x]}% , {votes} \n "
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {(total_votes)}")
print(f"-------------------------")
print(f"({candidates)})"
# print(f"Winner : {(winner)}")

#  Open the output file
with open(Final_Results.csv, "w") as datafile:
# Write the lines
    writer = csv.writer(datafile)
    writer.writerow("Election Results" + "\n")
    writer.writerow("-------------------------" + "\n")
    writer.writerow("Total Votes" + str(total_votes) + "\n")
    writer.writerow("-------------------------" + "\n")