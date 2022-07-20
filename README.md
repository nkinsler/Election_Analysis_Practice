# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties.
3. Calculate the voter turnout for each county.
4. Calculate the percentage of votes from each county.
5. Determine county with the highest turnout.
6. Get a complete list of candidates who received vots.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine winner of the election based on popular vote.

## Resources
- Data Source: [Election_Results.csv](https://github.com/nkinsler/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7 (64 bit), Visual Studio Code, 1.69.1 
- Python: [PyPoll_Challenge](https://github.com/nkinsler/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Election Audit Results
[Election_Results](https://github.com/nkinsler/Election_Analysis/blob/main/Analysis/election_results.txt)

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The Counties involved were:
  - Jefferson
  - Denver
  - Arapahoe
- The voter turnout per county were:
  - Jefferson county had 10.5% of the voters and 38,855 voters.
  - Denver county has 82.8% of the voters and 306,055 voters.
  - Arapahoe county has 6.7% of the voters and 24,801 voters.
- County with highest turnout:
  - Denver
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Election Audit Summary
The script used to determine the Colorado election can be utilized for any election with the results in a CSV file.  Two examples of how modify the script are as follows:
1. School elections were generally multiple seats are up for grabs.
  - We would track multiple winning candidates based on the number of seats available.
  - Example: 
    - Modify winning_candidate to winning_candidate1.
    - Add winning_candidate2 and so one for number of open seats.
    - ![School_Election1](https://github.com/nkinsler/Election_Analysis/blob/main/Resources/School_Election1.png)!
    - Determinin the winning vote counts could be expanded to rank the candidates and determining winning votes by creating a dictionary to pull from.
    - ![School_Election2](https://github.com/nkinsler/Election_Analysis/blob/main/Resources/School_Election2.png)!
 2. Modify the code to accomdate for seats.
  - Electoral college is a prime example where seats are assigned.
  - Example:
    - We would set each county participating with a set number of sets.
    - Such as
      - Jefferson_seats = 10 seats
      - Denver_seats = 17 seats
      - Arapahoe_seats = 8 seats
    - We would determine the winner of each county by using the code with a modification to run it for each county.
    - Once the results for each county are determined we would add the code to assign the seats to each county winner.
    - Finally, we would determine the seat winners off the sum of the seats won.
 Both examples above explain how the given code can be modified and applied to other election types.
