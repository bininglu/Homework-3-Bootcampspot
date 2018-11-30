import os
import csv
csvpath =os.path.join('.','Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    VoterID = []
    Vote = []
    Candidate = []

    for row in csvreader:
        VoterID.append(row[0])
        Vote.append(row[2])

    #The total number of votes cast
    TotalVote = len(VoterID)
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(TotalVote))
    print("-------------------------")

    #A complete list of candidates who received votes
    Candidate = list(set(Vote))

    Result_Count = []
    Result_Percent = []
    for n in range(0,len(Candidate)):
        #The total number of votes each candidate won
        Count = Vote.count(Candidate[n])
        Result_Count.append(Count)
        #The percentage of votes each candidate won
        Percent = Count/TotalVote
        Result_Percent.append ('{:.3%}'.format(Percent))


    #print (Candidate)
    #print (Result_Count)
    #print (Result_Percent)

    #Sort list by vote count
    Index=[]
    sorted_result=[]

    sorted_result=sorted(Result_Count,reverse=True)
    for num in sorted_result:
        Index.append(Result_Count.index(num))
    #print(Index)


    for i in Index:
        print(Candidate[i] + ": " + Result_Percent[i] + " (" + str(Result_Count[i]) + ")")

    #The winner of the election based on popular vote.
    Count_Max = max(Result_Count)
    Index_Max = Result_Count.index(Count_Max)
    Winner = Candidate[Index_Max]

    print("-------------------------")
    print("Winner: "+Winner)
    print("-------------------------")

