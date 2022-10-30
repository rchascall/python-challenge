# Dependencies
from calendar import month
from lib2to3.pgen2.token import PLUSEQUAL
import os
import csv
from pydoc import describe

# Data file path
budget_csv_path = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # Set all variables to 0
    total_months = 0
    grand_total_monthly = 0
    increase = 0
    decrease = 0
    change_inc = 0
    change_dec = 0
    pl_month_cur = 0
    pl_month_pre = 0
    ttlmonths = 0

    # List to store monthly change
    avg_change = []

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in (csvreader):
    
        # Count total Months
        ttlmonths = int(row[1])
        total_months = total_months + 1
    
        # Calculate total profit and loss (pl) from dataset
        monthly_pl = int(row[1])
        grand_total_monthly = grand_total_monthly + monthly_pl

        # Store previous profit/loss (pl) value equal as current value before resetting to next current
        pl_month_pre = pl_month_cur

        # Append change value to list containing monthly change values
        avg_change.append(change_inc)

        # Set Current Month Starting Point
        pl_month_cur = int(row[1])

        # Loop through to find Greatest Increase in Profits
        change_inc = pl_month_cur - pl_month_pre
        if change_inc > increase:
            increase = change_inc
            month_year_inc = (row[0])
            
        # Loop through to Find Greatest Decrease in Profits
        change_dec = pl_month_cur - pl_month_pre
        if change_dec < decrease:
            decrease = change_dec
            month_year_dec = (row[0])  

    # Add last value to List after exit from For loop
    avg_change.append(change_inc)
    
    # Loop through average change list to calculate Average Change - remove initial two erroneous values
    del avg_change[0]
    del avg_change[0]
    avg = sum(avg_change) / len(avg_change)
    
    # Print report heading and results
    print("Financial Analysis")
    print("-----------------------------------")
    print(f'Total Months: {total_months}')    
    print(f'Total: ${grand_total_monthly}')
    print(f'Average Change: ${avg:.{2}f}')
    print(f'Greatest Increase in Profits: {month_year_inc} (${increase})')
    print(f'Greatest Decrease in Profits: {month_year_dec} (${decrease})')

# Specify the file to write the results to for PyBank data
output_path = os.path.join("Analysis","PyBank_Results.csv")
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write Header Row
    csvwriter.writerow(['Measure', 'Date', 'Totals'])

    # Write Total Months Row
    csvwriter.writerow(['Total Months','',total_months])

    # Write Total Row
    csvwriter.writerow(['Total','',grand_total_monthly])

    # Write Average Change Row
    csvwriter.writerow(['Average Change','',avg])

    # Write Greatest Increase Row
    csvwriter.writerow(['Greatest Increase in Profits',month_year_inc,increase])

    # Write Greatest Decrease Row
    csvwriter.writerow(['Greatest Decrease in Profits',month_year_dec,decrease])


    

        

        
  
    