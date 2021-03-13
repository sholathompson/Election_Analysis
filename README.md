# Election-analysis

## Overview of Election Audit
Client will like an election audit of the tabulated results for US congressional precinct in Colorado. Analysis requested to report the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate and the winner of the election based on the popular vote. This task is usually done in Excel but our client would like to automate the process using Python. Final Python script will deliver the following information when the script is run: 
1.	Total number of votes cast
2.	A complete list of candidates who received votes
3.	Total number of votes each candidate received
4.	Percentage of votes each candidate won
5.	The winner of the election based on popular vote
6.	The voter turnout for each county
7.	The percentage of votes from each county out of the total count
8.	The county with the highest turnout

#Resources
- Data Source: election_resullts.csv
- Software: Python 2.7.16

## Election-Audit Results
The analysis of the election show that:
- There were 369,712 votes cast in this congressional election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGette received 73.8%  of the vote and 272,892 number of votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The winner of the election was:
	- Diana DeGette received 73.8%  of the vote and 272,892 number of votes
###### Screen shot of Election-Audit Results 
![Election Audit Results.png](https://github.com/sholathompson/Election_Analysis/blob/3e82930fca420bd01e10a3f98cf6e050a525f7bf/Election%20Audit%20Results.png)
## Election-Audit Summary 
The election audit successfully tabulated results for US congressional precinct in Colorado. The audit summary provided the results of an automated process using Python. Final Python script delivered identified that there were 369,712 total number of votes casted. Script also identified a complete list of candidates who received votes, total number of votes each candidate received, percentage of votes each candidate won and that the winner of the election based on popular vote was Diana DeGette. The voter turnout for each county and the percentage of votes from each county out of the total count revealed that Denver was the county with the highest turnout.
### Future Use of Script
In the future this code can be updated for use in the other congressional districts, senatorial districts and local elections. The script can be modified to input congressional districts, senatorial districts or local elections list and dictionary in place of county list and county votes dictionary. For Senatorial districts, in addition to the script to track the winning candidate, vote count and percentage we can add script to track whether the candidate is "Democrat" or "Republican".
