# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnder of the election based on popular vote
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save a file to a
# Open the election results and read the file.
with open(file_to_load) as election_data: 
   
# To do: read and analyze the data here
    # Print the file object.
     print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Arapahoe")
     txt_file.write("Denver")
     txt_file.write("Jefferson")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Write three counties to the file.
     txt_file.write("Arapahoe, Denver, Jefferson")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
     # Write three counties to the file.
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    for row in file_reader:
        print(row)
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties_options = []
county_voters ={}



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_turnout_county = ""
largest_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.

        county_name = row [1] 

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

        # If the candidate does not match any existing candidate add it to
        # the candidate list
if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
# And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

        # Add to the total vote count.
total_votes += 1

        # Print the candidate name from each row.
candidate_name = row[2]

        # If the candidate does not match any existing candidate...
if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
if candidate_name not in candidate_options:
            # Add it to the list of candidates.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

# Print the candidate vote dictionary.
print(candidate_votes)