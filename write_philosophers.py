from unicodedata import name


# This program writes three lines of data
 # to a file.
def main():
 # Open a file named philosophers.txt.
    outfile = open("philosophers.txt", "w")


 
# Write the names of three philosphers to the file – 
# John Locke, David Hume and Edmund Burke

    name1 = "John Locke"
    name2 = "David Hume"
    name3 = "Edmund Burke"

    outfile.write(name1 + '\n')
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')


# Close the file.
    outfile.close

# Call the main function.
main()
