#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:22:35 2018

@author: chloemayne
"""

import os
import csv

my_path1 = '/Users/chloemayne/Desktop/Homework/Instructions/PyPoll/Resources/election_data.csv'

# Open and read csv
with open(my_path1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    
    vote_count = 0
    
    candidates_list = []
    
    khan_votes = 0
    
    correy_votes = 0
    
    li_votes = 0
    
    otooley_votes = 0
    
    #Total number of votes cast
    for row in csvreader:
        
        #Total votes
        vote_count = vote_count + 1
        
         #Complete list of candidates who received votes
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        
        #Total number of votes each candidate won
        if row[2] == candidates_list[0]:
            khan_votes = khan_votes + 1
        
        elif row[2] == candidates_list[1]:
            correy_votes = correy_votes + 1
        
        elif row[2] == candidates_list[2]:
            li_votes = li_votes + 1
        
        else:
            otooley_votes = otooley_votes + 1
    
    
    #Percentage of votes each candidate won
    
    percentage_khan = round((khan_votes / vote_count*100), 3)
    percentage_correy = round((correy_votes / vote_count*100), 3)
    percentage_li = round((li_votes / vote_count*100), 3)
    percentage_otooley = round((otooley_votes / vote_count*100), 3)
  
    #Winner of the election based on popular vote.
    
    candidate_percent_list = []
    
    candidate_percent_list.append(percentage_khan)
    candidate_percent_list.append(percentage_correy)
    candidate_percent_list.append(percentage_li)
    candidate_percent_list.append(percentage_otooley)
    
    candidate_percent_list
   
    
    import operator
    max_index, max_value = max(enumerate(candidate_percent_list), key=operator.itemgetter(1))
    
    max_index
    
    winner = candidates_list[max_index]

    winner
   
    
    #Print script to terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(vote_count))
    print("-------------------------")
    print("Khan: " + str(percentage_khan) + "% (" + str(khan_votes) + ")")
    print("Correy: " + str(percentage_correy) + "% (" + str(correy_votes) + ")")
    print("Li: " + str(percentage_li) + "% (" + str(li_votes) + ")")
    print("O'Tooley: " + str(percentage_otooley) + "% (" + str(otooley_votes) + ")")
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")
  
output_file = '/Users/chloemayne/Desktop/python-challenge/PyPoll/main.txt'

    #Export a text file with the results.
with open(output_file, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(vote_count))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Khan: " + str(percentage_khan) + "% (" + str(khan_votes) + ")")
    txt_file.write("\n")
    txt_file.write("Correy: " + str(percentage_correy) + "% (" + str(correy_votes) + ")")
    txt_file.write("\n")
    txt_file.write("Li: " + str(percentage_li) + "% (" + str(li_votes) + ")")
    txt_file.write("\n")
    txt_file.write("O'Tooley: " + str(percentage_otooley) + "% (" + str(otooley_votes) + ")")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    