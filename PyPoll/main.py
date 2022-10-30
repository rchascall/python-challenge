# Dependencies
import os
import csv

# Data file path
election_data_csv_path = os.path.join("Resources","election_data.csv")

# Open and read csv
with open(election_data_csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # Set all variables
    total_votes = 0
    candidate = ""
    candidate_1 = "Charles Casper Stockham"
    candidate_count_1 = 0
    candidate_2 = "Diana DeGette"
    candidate_count_2 = 0
    candidate_3 = "Raymon Anthony Doane"
    candidate_count_3 = 0
    winning_candidate = ""

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Count total votes cast
    for row in (csvreader):

        # Count number of votes for each Candidate
        candidate = (row[2])
        if candidate == candidate_1:
            candidate_count_1 = candidate_count_1 + 1
            total_votes = total_votes + 1
        elif candidate == candidate_2:
            candidate_count_2 = candidate_count_2 + 1
            total_votes = total_votes + 1
        elif candidate == candidate_3:
            candidate_count_3 = candidate_count_3 + 1
            total_votes = total_votes + 1

# Calculate Winner
if candidate_count_1 > candidate_count_2 and candidate_count_1 > candidate_count_3:
    winning_candidate = candidate_1
elif candidate_count_2 > candidate_count_3:
    winning_candidate = candidate_2
else:
    winning_candidate = candidate_3

# Print report heading and results
print("Election Results")
print("-----------------------------------")        
print(f'Total Votes Cast: {total_votes}')
print("-----------------------------------")
print(f'{candidate_1}: {(candidate_count_1 / total_votes)*100:.{3}f}% ({candidate_count_1})')
print(f'{candidate_2}: {(candidate_count_2 / total_votes)*100:.{3}f}% ({candidate_count_2})')
print(f'{candidate_3}: {(candidate_count_3 / total_votes)*100:.{3}f}% ({candidate_count_3})')
print("-----------------------------------")
print(f'Winner: {winning_candidate}')
print("-----------------------------------")

# Specify the file to write the results to for PyPoll data
output_path = os.path.join("Analysis","PyPoll_Results.csv")
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write Total Votes Row
    csvwriter.writerow(["Total Votes Cast",total_votes])

    # Write Header Row
    csvwriter.writerow(['Candidate', 'Percent of Vote', 'Total Votes Received'])

    # Write Candidate 1 Row
    csvwriter.writerow([candidate_1,(candidate_count_1/total_votes*100),candidate_count_1])

    # Write Candidate 2 Row
    csvwriter.writerow([candidate_2,(candidate_count_2/total_votes*100),candidate_count_2])

    # Write Candidate 3 Row
    csvwriter.writerow([candidate_3,(candidate_count_3/total_votes*100),candidate_count_3])

    # Write Winner Row
    csvwriter.writerow(["Winner",winning_candidate])
   
