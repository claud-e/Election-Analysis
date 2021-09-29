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
with open(file_to_load) as election_data:


    #Perform analysis
    file_reader = csv.reader(election_data)
    #print headers
    headers=next(file_reader)
    print(headers)



with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")

#Close outfile

txt_file.close()
#Close file
election_data.close()
