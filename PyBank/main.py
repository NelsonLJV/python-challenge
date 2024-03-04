#Import dependencies
import os
import csv

#Store filepath
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create lists where data will be stored
months = []
profit_loss =  []
diff = []

#Open and read csv
with open(csvpath) as csvfile:

    #Specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read header first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total = 0
    
    #Read through the rows of data, excluding the header
    for row in csvreader:

      #Add the Date and Profit/Losses values
       months.append(row[0])
       profit_loss.append(int(row[1]))
       total += int(row[1]) 
       
    #Calculate changes in Profit/Losses and store them in a separate list
    for i in range(1, len(months)):
            change = profit_loss[i]-profit_loss[i-1]
            diff.append(change) 

    #Calculate the average, max, and min
    Average = sum(diff)/len(diff)
    Max = max(diff)
    Min = min(diff)

    #Index location of the max and min values
    max_row = diff.index(max(diff))
    min_row = diff.index(min(diff))
    
#Print the analysis   
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(len(months)))
print("Total: " + "$"+ str(total))
print("Average Change:"+"$"+str(round(Average,2)))
print("Greatest Increase in profits: " + str(months[max_row +1]) + " " + str(Max))
print("Greatest Decrease in profits: " + str(months[min_row +1]) + " " + str(Min))

#Output path save
output_file = os.path.join('analysis','results.txt')

#Export output results
with open(output_file, "w", newline='') as datafile:
     datafile.write(f"Financial Analysis\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Total Months:  {len(months)}\n")
     datafile.write(f"\n")
     datafile.write(f"Total:  ${str(total)}\n")
     datafile.write(f"\n")
     datafile.write(f"Average Change:  ${str(round(Average,2))}\n")
     datafile.write(f"\n")
     datafile.write(f"Greatest Increase in Profits: {months[max_row +1]} (${str(Max)})\n")
     datafile.write(f"\n")
     datafile.write(f"Greatest Decrease in Profits: {months[min_row +1]} (${str(Min)})\n")