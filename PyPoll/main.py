import csv
import os

# Define the path to the election data CSV file
csv_file_path = os.path.join("resources", "election_data.csv")

# Create a dictionary to store candidate data
candidate_data = {}

# Read the election data from the CSV file
with open(csv_file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Process the election data
    for row in csvreader:
        candidate_name = row[2]

        # Update or add candidate information in the dictionary
        if candidate_name in candidate_data:
            candidate_data[candidate_name]["votes"] += 1
        else:
            candidate_data[candidate_name] = {"votes": 1}

# Calculate the total number of votes cast
total_votes_cast = sum(candidate_info["votes"] for candidate_info in candidate_data.values())

# Determine the election winner
winner = max(candidate_data, key=lambda x: candidate_data[x]["votes"])

# Define the path to the output text file
output_file_path = os.path.join("analysis", "election_results.txt")

# Create and write the election results to the text file
with open(output_file_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes Cast: {total_votes_cast}\n")
    txtfile.write("-------------------------\n")
    for candidate, info in candidate_data.items():
        vote_percentage = (info["votes"] / total_votes_cast) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({info['votes']})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print("Election results have been saved to 'analysis/election_results.txt'.")
