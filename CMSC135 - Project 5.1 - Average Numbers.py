# Write a program the calculates the average of all the numbers
# stored in the file. Assume a file containing a series of integers is
# named numbers.txt and exists on the computer disk.
#
# This program will read numbers.txt and will calculate the average,
# which will require adding them up and then dividing by the number of
# data points summed. This will require that the program can identify
# how many data points have been added.
# First the program will need to open numbers.txt, read numbers.txt, and
# the close numbers.txt. The contents of numbers.txt will be stores in a
# middleman variable, which will be called "middleman".


# define the main function
def main():
    # call the function to open, read, close numbers.txt
    access()

    print("End of Line. (main)")

def access():
    # Open numbers.txt
    middleman = open("numbers.txt", 'r')

    # Read numbers.txt
    fileContents = middleman.read()

    # Close numbers.txt
    middleman.close()

    print("End of Line. (access)")

# run main
main()

print("End of Line. (program)")
