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

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {(total_votes)}")
    print(f"-------------------------")
    print(f"({candidates)})"


    # # Set variable for output file
    # Final_Results = os.path.join("Final_Results.csv")

    # #  Open the output file
    # with open(Final_Results, "w") as datafile:
    #     writer = csv.writer(datafile)

    #     # Write the lines
    #     datafile.write("Election Results" + "\n")
    #     datafile.write("-------------------------" + "\n")
    #     datafile.write("Total Votes" + str(total_votes) + "\n")
    #     datafile.write("-------------------------" + "\n")