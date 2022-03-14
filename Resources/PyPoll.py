# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Add Dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0
# Candidate  options
candidate_options = []
# Candidate votes empty dictionary
candidate_votes = {}

# Winning candidate and winniing Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        # 2 Add to the total vote count
        total_votes +=1  
        # Print candidate  name for each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

             # Add it to the list of candidates.
            candidate_options.append(candidate_name)

              # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # 3. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1 

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Use a for loop to iterate through the candidate_options = [] list. We will get the candidate's name.
    for candidate_name in candidate_votes:
         # 2  Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results) 

        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count, candidate, and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #Print winning candidates results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)