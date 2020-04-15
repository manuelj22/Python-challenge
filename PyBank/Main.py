import os
import csv

csvpath = os.path.join(".", "PyBank", "Resources","budget_data.csv")

with open(csvpath, 'r', newline='') as csvfile:    
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    Dates = []
    TotalRev = 0
    MaxProfit = 0
    MinProfit = 0
    
    for row in csvreader:
        Dates.append(row[0])
    
        TotalRev += int(row[1])

        if(MaxProfit<int(row[1])):
            MaxProfit = int(row[1])
            MaxProfitMonth = row[0]
        
        if(MinProfit>int(row[1])):
            MinProfit = int(row[1])
            MinProfitMonth = row[0]
    
    print("\nFinancial Analysis\n-----------------------------------------------")
    print(f"Total Month: {len(Dates)}")
    print(f"Total Revenue : ${TotalRev}")
    print(f"Average Change : ${round(TotalRev/len(Dates),2)}")
    print(f"Greatest Increase in Profits : {MaxProfitMonth} ({MaxProfit})")
    print(f"Greatest Decrease in Profits : {MinProfitMonth} ({MinProfit})")

file = open('PyBank.txt','w')

file.write("Financial Analysis")
file.write("\n-----------------------------------------------")
file.write("\nTotal Month: " + str(len(Dates)))
file.write("\nTotal Revenue : $" + str(TotalRev))
file.write("\nAverage Change : $" + str(round(TotalRev/len(Dates),2)))
file.write("\nGreatest Increase in Profits : " + str(MaxProfitMonth) + " (" + str(MaxProfit) + ")")
file.write("\nGreatest Decrease in Profits : " + str(MinProfitMonth) + " (" + str(MinProfit) + ")")

file.close()