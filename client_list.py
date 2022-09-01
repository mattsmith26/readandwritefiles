def main():

 # Open a file named philosophers.txt.
    infile = open("clients.txt", "r")


    i = 0
    for line in infile:
        i += 1
        print(str(i) + ".  " + line.rstrip("\n"))
        
    # ^^ or you can use print(counter, ". ", line.rstrip('\n'), sep='')

    
 # Call the main function.
main()