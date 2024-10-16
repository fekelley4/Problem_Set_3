#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3
#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        continue

    #Split the data into values
    lineData = lineString.split(',')
    
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]
    #Extract the fleet value
    fleet = lineData[fleet_idx]
    
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

# Check dictionary length
len(vesselDict)


#%% Task 4.4

# Assigns the string value 440196000 to a variable named vesselID
vesselID = "440196000"

# Uses the vesselDict dictionary to lookup the fleet value for the vessel with the MMSI equal to the vesselID value.

#Loop through items in vesselDict

for mmsi, fleet in vesselDict.items(): 
    #Use an if statement to determine if the current state is 'Texas'
    if mmsi == vesselID: 
        # Print the dictionary value corresponding with the state
        print(f"Vessel #{vesselID} flies the flag of {fleet}.")
        # End if loop
        break
    

#%% Task 5 -- Open file
# Open the loitering_events_20180723.csv file into a file object variable. 
# Construct a list of all lines in the csv file.

#Create a Python file object
fileObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#%% Task 5 -- Loop through each data line & Create Variables
# Loop through each data line (i.e. skip the header line) 
# Split the line string into a list of data items.

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, start/end latitude, and start/end longitude values
transshipment_mmsi_idx = headerItems.index('transshipment_mmsi')
start_lat_idx = headerItems.index('starting_latitude')
end_lat_idx = headerItems.index('ending_latitude')
start_long_idx = headerItems.index('starting_longitude')
end_long_idx = headerItems.index('ending_longitude')

#%% Task 5
# Store the transshipment_mmsi, starting & ending latitude, and starting & ending longitude values into their own respective variables
# Examines the starting and ending latitude (the 2nd and 4th columns in the csv) to determine whether the event crosses the equator, passing from the southern hemisphere to the north.
# Examines the starting longitude to see whether it falls between 145°E and 155°E. Again, it’s useful to create a Boolean variable that store whether this is true or false.
# If both the latitude and longitude constraints are true, then use the value of the transmission_mmsi for the current line to query the vesselsDict created above to print the vessel’s mmsi and its fleet.

# Create a variable to determine if vessels meet criteria
vessels_met_criteria = False

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        continue

    #Split the data into values
    lineData = lineString.split(',')
    
    #Extract the values from the list 
    mmsi = lineData[transshipment_mmsi_idx]
    start_lat = float(lineData[start_lat_idx])
    end_lat = float(lineData[end_lat_idx])
    start_long = float(lineData[start_long_idx])
    end_long = float(lineData[end_long_idx])

    # Variable defining event crossing an equator 
    crossing_equator = start_lat < 0 and end_lat > 0
    # Variable defining longitude range
    long_range = 145 <= start_long <= 155

    # Checking if the two condtions are met
    if crossing_equator and long_range:
        # get() retrieves fleet value corresponding to mmsi value
        fleet = vesselDict.get(mmsi, 'Unknown')
        print(f"Vessel #{mmsi} {start_long} flies the flag of {fleet}.")
        # set criteria variable to true, indicating the specified conditions have been met
        vessels_met_criteria = True


# BONUS: If no vessels meet your criteria, print a message that states “No vessels met criteria”
if not vessels_met_criteria:
    print("No vessels met criteria")


# %%
