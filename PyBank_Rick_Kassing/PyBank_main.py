import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('PyBank_Resources', 'budget_data.csv')


# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    first_row = next(csvreader)
    x = first_row[1]
    total_months=[]
    total_dollars=[]
    profit=[]
    profit_change_list=[]
    total_profit=[]
    greatest_increase=[]
    greatest_decrease=[]
    prevous_profit= 0
    i=1
    total_months.append(int(x))
    total_dollars.append(int(x)) 

    for row in csvreader:
    # Sum for number of months and total $
        total_dollars.append(int(row[1]))
        total_months.append(row[0])        

    # Find the "profit_change" for each month
        profit_change = int(total_dollars[i]) - int(total_dollars[i-1])
    
        profit_change_list.append(int(profit_change))
# Calaculate the total profit for the average calc
        total_profit = sum(profit_change_list)
# Calaculate the average profit Chg
        average_change = (sum(profit_change_list))/len(total_months)
        i+=1
# Calculate greatest_increase 
    greatest_increase=max(profit_change_list)
    greatest_increase_month= total_months[profit_change_list.index(greatest_increase)+1]

    # Calculate greatest_decrease   
    greatest_decrease= min(profit_change_list)
    greatest_decrease_month= total_months[profit_change_list.index(greatest_decrease)+1]
    
  # Print Statements  
    print(f"Financial Analysis")
    print (f"---------------------")
    print(f"Total months: {len(total_months)}")
    print(f"Total $: {sum(total_dollars)}")
    print(f"Average Change : {round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${(greatest_decrease)})")

    datafile.write("Financial Analysis" + "\n")
    datafile.write("---------------------------" + "\n")
    datafile.write(f"Total Months: {(total_month)}" + "\n")
    datafile.write(f"Total: ${(total)}" + "\n")
    datafile.write(f"Average Change: ${round(average_change),2}" + "\n")
    datafile.write(f"Great Increase in Profits: {greatest_increase_month} (${(greatest_increase)})" + "\n")
    datafile.write(f"Great Decrease in Profits: {greatest_decrease_month} (${(greatest_decrease)})" + "\n")