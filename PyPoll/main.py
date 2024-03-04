#Import dependencies
import os
import csv

#Store filepath
csvpath = os.path.join('Resources', 'election_data.csv')

#Create lists where data will be stored
ballotid = []
candidate =  []
candidate1 = []
candidate2 = []
candidate3 = []

#Open and read csv
with open(csvpath) as csvfile:

    #Specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read header first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Store candidate names as variables
    charles = "Charles Casper Stockham"
    diana = "Diana DeGette"
    raymon = "Raymon Anthony Doane"
    
    #Read through the rows of data, excluding the header
    for row in csvreader:

      #Add ballotid and candidates
       ballotid.append(row[0])
       candidate.append(str(row[2]))

#Loop through each value to get the amount of votes for each candidate
for votes in candidate:
    if votes == charles:
         candidate1.append(votes)

for votes in candidate:
    if votes == diana:
         candidate2.append(votes)

for votes in candidate:
    if votes == raymon:
         candidate3.append(votes)

#Changing the values to percentages 
percent_charles = (len(candidate1)/len(ballotid))*100

percent_diana = (len(candidate2)/len(ballotid))*100

percent_raymon = (len(candidate3)/len(ballotid))*100

#Finally calculate the winner based off of the percetnages with an if statement
if (percent_charles > percent_diana and percent_charles > percent_raymon):
        winner = charles
       
elif (percent_diana > percent_charles and percent_diana > percent_raymon):
        winner = diana
        
else:
        winner = raymon
        
        
#Print the results
print("Election Results")
print("----------------------------")
print("Total Votes: "+ str(len(ballotid)))
print("------------------------------")
print(str(charles) + ": " + str(round(percent_charles,3)) + "% " + str(len(candidate1)))
print(str(diana) + ": " + str(round(percent_diana,3)) + "% " + str(len(candidate2)))
print(str(raymon) + ": " + str(round(percent_raymon,3)) + "% " + str(len(candidate3)))
print("------------------------------")
#Print winner using the voters sorted becuase the candidates are in a  descending order.
print("Winner: "+ str(winner))
print("----------------------------")


#Output path save
output_file = os.path.join('analysis','results.txt')

#Print output results
with open(output_file, "w", newline='') as datafile:
     datafile.write(f"Election Results\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Total Votes:  {len(ballotid)}\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"{charles}: {str(round(percent_charles,3))}% ({len(candidate1)})\n")
     datafile.write(f"\n")
     datafile.write(f"{diana}: {str(round(percent_diana,3))}% ({len(candidate2)})\n")
     datafile.write(f"\n")
     datafile.write(f"{raymon}: {str(round(percent_raymon,3))}% ({len(candidate3)})\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")
     datafile.write(f"\n")
     datafile.write(f"Winner: {winner}\n")
     datafile.write(f"\n")
     datafile.write(f"------------------------\n")

