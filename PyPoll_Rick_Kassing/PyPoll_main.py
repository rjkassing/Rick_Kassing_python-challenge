import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('.', 'Resources', 'election_data')

csvreader = csv.reader(csvfile.delimiter)

# List of candidates
list1 = [ 'Correy', 'Khan', 'Li', 'OTooley']

# Count votes per candidate
Correy_count = list1.count('Correy')
Khan_count = list1.count('Khan')
Li_count = list1.count ('Li')
OTooley_count = list1.count ('OTooley')

    df.head()

        df['Voter ID'].value_counts()


    # Total Total Number of Votes
    Vote_Count = 

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {str(win_percent)}")
    print(f"LOSS PERCENT: {str(loss_percent)}")
    print(f"DRAW PERCENT: {str(draw_percent)}")
    print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)
