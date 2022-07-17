# Add our dependencies
import csv
import os

# Assign a variable to load file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Addisgn a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_Analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    
    # Read the fle object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)

# Close the file.
election_data.close()

# Total number of votes cast

# A complete list of candidates who received votes

# Total number of votes each candidate received

# Percentage of votes each candidate won

# The winner of the election based on popular vote