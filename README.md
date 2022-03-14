# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election

The data we need to retrieve includes:
  1. The total number of votes cast
  2. A complete list of candidates who received votes 
  3. The percentage of votes each candidate won
  4. The total number of votes each candidate  won
  5. The winner of the election based on popular vote

## Resources
- Data source: [Election Results](https://github.com/mxndyy/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.6, VS Code 1.65

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was: 
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes

## Challenge Overview
In addition to the information above The election commission requested additional data to complete the audit which includes:
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
 
## Challenge Results
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- Denver had the largest number of votes



![Resources/Results](/Resources/Results.png)

## Election-Audit Summary
The script provided for this election audit can be altered to fit any other type of election. For example, in this election we were looking at the results by county, however we could look at results by state or city on a bigger scale of elections such as presidential elections. We would just need to ensure that the data is available in a .csv file or other compatible file. We would also be able to add more information such as voter political parties and voter ages. 
