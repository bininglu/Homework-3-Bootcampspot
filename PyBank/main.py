import os
import csv
csvpath =os.path.join('.','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    Date = []
    ProfitLoss = []
    Change = []
    print("Financial Analysis")
    print("----------------------------")
    for row in csvreader:
        Date.append(row[0])
        ProfitLoss.append(int(row[1]))

    #The total number of months included in the dataset
    Month_Total=len(Date)
    print("Total Months: "+ str(Month_Total))

    # The total net amount of "Profit/Losses" over the entire period
    Total=sum(ProfitLoss)
    print("Total: $"+ str(Total))

    for count in range(1,Month_Total):
        Change.append(ProfitLoss[count]-ProfitLoss[count-1])

    #The average change in "Profit/Losses" between months over the entire period
    Change_Ave=sum(Change)/len(Change)
    print("Average  Change: $"+ "%.2f" % Change_Ave)

    #The greatest increase in profits (date and amount) over the entire period
    Change_Max=max(Change)
    Index_Max=Change.index(Change_Max)
    Month_Max=Date[Index_Max+1]
    print("Greatest Increase in Profits: "+ Month_Max + " ($" + "%.2f" % Change_Max + ")")

    #The greatest decrease in losses (date and amount) over the entire period
    Change_Min=min(Change)
    Index_Min=Change.index(Change_Min)
    Month_Min=Date[Index_Min+1]
    print("Greatest Decrease in Profits: "+ Month_Min + " ($" + "%.2f" % Change_Min + ")")

