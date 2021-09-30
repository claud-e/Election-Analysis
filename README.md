# Election-Analysis

## Overview of Election Audit
The Colorado Board of Elections has requested an audit of their last congresional elections to determine vote distribution and the winner. They have provided a csv file with the data and expect us to conduct a fair assessment of the situation and report it. The people in charge have requested this process to be done in python so that future counts might be done automatically.

## Election-Audit Results:

To see a complete summary of these questions please refer to the image at the end of this section.

- How many votes were cast in this congressional election?

    369,711

- Provide a breakdown of the number of votes and the percentage of total votes por each county in the precinct.

    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)


- Which county had the largest number of votes?

    Denver

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    Charles Casper Stockham: 23.0% (85,213)

    Diana DeGette: 73.8% (272,892)

    Raymon Anthony Doane: 3.1% (11,606)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%


![Election-Audit Results](https://github.com/claud-e/Election-Analysis/blob/main/Screen%20Shot%202021-09-29%20at%2020.49.43.png)

## Election-Audit Summary:
- Business proposal on how to modify this code for future elections. At least 2 examples.

1. One potentially interesting piece of information is the relationship between counties and candidates. For this, 3 new dictionaries (one for each candidate) could be defined in which the keys are the names of the counties and the values are the votes each person received in each county, for example:

````
candidate1_votes={}
candidate2_votes={}
candidate3_votes={}
...
...
...
for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name=row[1]

        if candidate_name == "Diana DeGette":
            
             candidate1_votes[county_name]+=1
        
        elif candidate_name == "Charles Casper Stockham":

            candidate2_votes[county_name]+=1
...
            

````
With a code similar to this the distribution of voters could be explored and potential gerrymandering exposed.


2. The current voting method is commonly known as First Past the Post (FPtP), it consists of giving voters a single vote which then is assigned to one candidate, in the end the candidate with the most votes wins. This is a heavily criticized system which overtime results in poor representation and only 2 parties, for more information refer to the next video: [The Problems with First Past the Post Voting Explained](https://www.youtube.com/watch?v=s7tWHJfhiyo&list=PL7679C7ACE93A5638&t=0s)

One way to improve voter representation is to adopt a system like Single Transferable Vote (STV), in which a single voter can rank the candidates they want to vote for, effectively giving them the chance to vote as many times as there are candidates. If such a system were to be adopted the first thing to do would be to change the csv files and add more columns in the order of the votes as in the next table:

| voter ID | County | Candidate 1 | Candidate 2 | Candidate 3 |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| xxxxxx | County_name | Candidate_name | Candidate_name | Candidate_name |

Given the fact that this is in fact a Dataframe, Pandas would be the best tool to work on this process, but this might be better explained in a different project.



