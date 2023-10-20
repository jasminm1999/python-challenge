import os
import csv

# Path to the CSV file
csv_path = os.path.join("LearningPython/python-challenge/PyPoll/Resources/election_data.csv")

# Variables to store election analysis results
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file and tally the votes
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Extract candidate name from the row
        candidate_name = row[2]
        
        # If the candidate is not in the dictionary, add them with 1 vote
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            # If the candidate is already in the dictionary, increment their vote count
            candidates[candidate_name] += 1

# Find the winner and calculate the percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the election analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join("LearningPython/python-challenge/PyBank/analysis/election_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results have been written to the '{output_path}' file.")
