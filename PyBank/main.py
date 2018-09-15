#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:51:40 2018

@author: chloemayne
"""
     
import os
import csv

my_path1 = '/Users/chloemayne/Desktop/Homework/Instructions/PyBank/Resources/budget_data.csv'

# Open and read csv
with open(my_path1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

   #Set counter for total # of months in the dataset
    counter = 0
    
    #Set counter for profit/ losses total
    profit = 0
    
    revenue_change = 0
    
    increase = ["", 0]
    decrease = ["", 1]
    
    profit_changes_list = []
    
    for row in csvreader:
         
        #Calculate total number of months included in the dataset
        counter = counter + 1
        
        #Calculature total net amount of "Profit/Losses" over the entire period
        profit = profit + int(row[1])
        
        #Calculate change in "Profit/Losses" between months over the entire period
        profit_change = int(row[1]) - revenue_change
        revenue_change = int(row[1])
        
        #Ad to profit changes list []
        profit_changes_list.append(profit_change)

        #Calculate greatest increase in profits (date and amount) over the entire period
        if (profit_change > increase[1]):
            increase[1] = profit_change
            increase[0] = row[0]

        #Calculate greatest decrease in losses (date and amount) over the entire period
        if (profit_change < decrease[1]):
            decrease[1] = profit_change
            decrease[0] = row[0]

    #Find average revenue of list
    print(profit_changes_list)
    
    sum_of_profit_changes = sum(profit_changes_list)
    
    print(sum_of_profit_changes)
    
    len_of_profit_changes = len(profit_changes_list)
    
    print(len_of_profit_changes)
    
    avg_changes = round(sum_of_profit_changes / len_of_profit_changes)
    
    print(avg_changes)
    
    
   #Print the analysis to the terminal.
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(counter))
    print("Total: $" + str(profit))
    print("Average Change: $" + str(avg_changes))
    print("Greatest Increase in Profits: " + str(increase[0]) + " ($" + str(increase[1])+ ")")
    print("Greatest Decrease in Profits: " + str(decrease[0]) + " ($" + str(decrease[1])+ ")")


output_file = '/Users/chloemayne/Desktop/python-challenge/PyBank/main.txt'

    #Export a text file with the results.
with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(counter))
    txt_file.write("\n")
    txt_file.write("Total: $" + str(profit))
    txt_file.write("\n")
    txt_file.write("Average Change: $" + str(avg_changes))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(increase[0]) + " ($" + str(increase[1])+ ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(decrease[0]) + " ($" + str(decrease[1])+ ")")
    
    
    