import os
import csv

TotalVotes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes = 0

csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath,'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        
        TotalVotes += 1
        
        if (row[2] == "Khan"):
            KhanVotes += 1
        elif (row[2] == "Correy"):
            CorreyVotes += 1
        elif (row[2] == "Li"):
            LiVotes += 1
        else:
            OtooleyVotes += 1
            
    KahnPercent = KhanVotes / TotalVotes
    CorreyPercent = CorreyVotes / TotalVotes
    LiPercent = LiVotes / TotalVotes
    OtooleyPercent = OtooleyVotes / TotalVotes
    
    Winner = max(KhanVotes, CorreyVotes, LiVotes, OtooleyVotes)

    if Winner == KhanVotes:
        WinnerName = "Khan"
    elif Winner == CorreyVotes:
        WinnerName = "Correy"
    elif Winner == LiVotes:
        WinnerName = "Li"
    else:
        WinnerName = "O'Tooley" 

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"---------------------------")
print(f"Kahn: {KahnPercent:.3%}({KhanVotes})")
print(f"Correy: {CorreyPercent:.3%}({CorreyVotes})")
print(f"Li: {LiPercent:.3%}({LiVotes})")
print(f"O'Tooley: {OtooleyPercent:.3%}({OtooleyVotes})")
print(f"---------------------------")
print(f"Winner: {WinnerName}")
print(f"---------------------------")

output_file = os.path.join('.', 'PyPoll', 'PyPoll.txt')

with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {TotalVotes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {KahnPercent:.3%}({KhanVotes})\n")
    txtfile.write(f"Correy: {CorreyPercent:.3%}({CorreyVotes})\n")
    txtfile.write(f"Li: {LiPercent:.3%}({LiVotes})\n")
    txtfile.write(f"O'Tooley: {OtooleyPercent:.3%}({OtooleyVotes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {WinnerName}\n")
    txtfile.write(f"---------------------------\n")