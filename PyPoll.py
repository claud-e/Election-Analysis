#Data to retrieve

#1. total number of votes cast
#2. a complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#path to the poll: election_results.csv

import csv
import os

#Assign variable for the file to load and the path

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
total_votes=0
candidate_options=[]
candidate_votes={}
candidate_results=""

#Victory tracker
winner=""
winning_count=0
winning_percentage=0
with open(file_to_load) as election_data:


    #Perform analysis
    file_reader = csv.reader(election_data)
    #print headers
    headers=next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #print(row)
        total_votes+=1
        #reading candidate names per row
        candidate_name=row[2]
        #adding candidate names to candidate option list only if it is not yet in it
        if candidate_name not in candidate_options:
            #Make list of candidates
            candidate_options.append(candidate_name)
            #Initialize variable
            candidate_votes[candidate_name]=0
        #Start counting votes
        candidate_votes[candidate_name]+=1
with open(file_to_save, "w") as txt_file:
         
        election_results=(f"\nElection Results\n------------\nTotal Votes: {total_votes}\n--------------\n")

        print(election_results,end="")
        txt_file.write(election_results)

        #print(f"total votes: {total_votes}")
        for candidate_name in candidate_votes:
            votes=candidate_votes[candidate_name]
            vote_percentage=float(votes)/float(total_votes)*100
        # print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the votes")
            candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            
            
            
            #Determine winning vote count, winning percentage and winner
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winner=candidate_name
        #Print winner to terminal
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        txt_file.write(winning_candidate_summary)
       
        
        
        
        
    # print(winning_candidate_summary)

        # print(candidate_votes)
        
    



#Close outfile

txt_file.close()
#Close file
election_data.close()
