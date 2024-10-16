#%% Task 1 - Edit code to print as requested

# Assign variables
mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

# Print in desired format 
print (mountain + ", sometimes called ")
print('\"' + nickname + '\",')
print("is " + str(elevation) + "\' above sea level.")

#%% Task 2 - Lists and Iteration

# Create a variable pointing to the data file
data_folder = 'W:/859_data/triangle'
# Print the string object
print(data_folder)

# Create a list object
data_list = ['streams.shp', 'stream_types.cvs', 'naip_imagery.tif']

# Assign variable equal to string
user_item = 'roads.shp'

# Add user_item to list object
data_list.append(user_item)

# Loop through list and print full data path
for x in data_list:
    print(data_folder + "/" + x)

#%% Task 3 - Lists and Iteration

# Create empty list variable 
user_numbers = []

# For loop that will ask for an integer three times
for x in range(3):
    # Create user prompt
    user_input = input("Enter an integer: ")
    # Creates an integer object for input values
    input_integers = int(user_input)
    # Add input values to list object 
    user_numbers.append(input_integers)

# Sort input values 
user_numbers.sort()
# Print highest value
print("Highest Input Value: ", user_numbers [-1])

#%% Task 3 - Challenge 

# Create empty list variable 
user_numbers = []

# For loop that will ask for an integer three times
for x in range(3):
    # Create user prompt
    user_input = input("Enter an integer: ")
    # Creates an integer object for input values
    input_integers = int(user_input)
    # Add input values to list object 
    user_numbers.append(input_integers)

# Sort input values in descending order
user_numbers.sort(reverse=True)
# Print sorted values 
print("Sorted values: ", user_numbers)

# %%
