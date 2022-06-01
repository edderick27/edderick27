# prompt user for directory
directory = input("Enter dicrectory to save file: ")
# directory defaults to current directory if user presses enter key
if directory == "":
    directory = "."
# checks that path is valid
assert os.path.exists(directory), "Path does not exist."

# prompt user for filename
filename = input("Enter filename: ")

# prompt for user details
name = input("Enter name: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

# create file object to write to specified file in directory
with open("{}/{}.csv".format(directory, filename), 'w') as file:
    # write user details to file
    file.write(",".join([name, address, phone]) + "\n")

# create file object to read from specified file in directory
with open("{}/{}.csv".format(directory, filename), 'r') as file:
    print("{}/{}.csv contents".format(directory, filename))
    # loop through each line in file and print to screen
    for line in file:
        print(line)
