#Nikolas Bekris
#CSC110
#6/12/16

#This program simulates a one dimensional cellular automaton. Using a list, it
#imports a pattern from a text file that the user specifies. Using this pattern
#it creates a list and using a loop, simulates cell death and life using 1s and 0s.


#function opens file and asks for the text file name from the user. 
#If the file name doesn't exist the program prompts the user for input again.
#This input is than returned to the read_file function.
def usr_input():

    #Print statements that introduce user to the program
    print ('Welcome! This program simulates one dimensional cellular automaton.')
    print ('Using rules from a text file, it will generate this simulation.')
    stop = -1 #exit sentinal
    while stop == -1:
        try:
            usr_file = open (input("Please enter a file name.") + '.txt')
            stop = 1
        except FileNotFoundError:
            print ("Sorry, that file could not be found.")
            stop = -1
    return usr_file


#function prompts and checks if user input for number of steps is a negative
#number until it is a positive number.Then returns this input to the main function.
def step_val():
    
    chksteps = input("Please enter the number of steps.")
    while int(chksteps) < 0: #loops until variable is more than 0.
        chksteps = input("Please enter a positive number.")
    return chksteps

#function reads file that user inputs. Calls the usr_input function to open file.
#creates a list with a pattern from the text file and returns this list.
def read_file():
    
    rules = usr_input()
    rules_list = []
    line = rules.readline()
    line = line.rstrip("\n") #strips space from text file line

    #loop that reads each line in text file.
    while line != "":
        if line.lower() == "alive": #describes state of cell
            state = 1
            rules_list.append(state) #appends this state to empty list as a 1
        elif line.lower() == "dead":
            state = 0
            rules_list.append(state)
        elif line.isdigit() == True:
            cellLen = int(line) #variable that decides how long list will be
            rules_list.append(cellLen)      
        line = rules.readline()
        line = line.rstrip("\n")
    return rules_list

#function calls read_file and takes list that it created. elements in this list
#are used to create a new list that will simulate automaton. function then returns
#this new list to the main function.
def create_list():
                   
    rules = read_file() #gets list from read_file function
    cellLen = rules[3] #decides how long new list is
    index = 0
    game_list = []

    #loop that creates new list based on list from read_file
    while index < len(rules):
        if rules[index] == 1:
            for n in range(cellLen):
                game_list.append(1)
        elif rules[index] == 0:
            for n in range(cellLen):
                game_list.append(0)
        index += 1
    return game_list


#main function that calls create_list function and gets a list from it. Also calls
#step_val function to get number of steps from user. Using these it calls a print function
#to output the cell autmaton simulation.
def main():
    
    lst = create_list()
    steps = step_val()
    count = 0
    print (format_list(lst)) #calls the format_list function, then prints
    
    #loop that goes for however many steps the user inputs.
    while count < int(steps):
        newlst = []
        i = 0

        #this loop is the cell automaton simulation
        while i < len(lst):
            if i == 0:
                if lst[i] == 0 and lst[i + 1] == 0: #test for cell at index 0 that has dead cells as its neighbors
                    newlst.append(1)
                else:
                    newlst.append(0)
            elif i >= 1: #test for cell that is not neighborless
                try: #try/except statements; test for cell state.
                    if lst[i] == lst[i + 1] and lst[i] == lst[i - 1] and lst[i - 1] == lst[i + 1]:
                        newlst.append(1)
                    else:
                        newlst.append(0)
                except IndexError: #except statement for when cell has no neighbor to its right
                    try:
                        if lst[i + 1] == 0:
                            newlst.append(1)
                        else:
                            newlist.append(0)
                    except IndexError: 
                        if lst[i - 1] == 0 and lst[i] == 0:
                            newlst.append(1)
                        else:
                            newlst.append(0)
                            
            i += 1
        count += 1
        print (format_list(newlst))
        lst = newlst
    print ('Simulation Complete!')

#function formats list from main so it can be printed in a more user friendly way.
#changes 1s to '+' and 0s to '' and replaces commas with spaces. returns this new
#formated list to main where it gets printed.
def format_list(newlst):
    
    display_lst = []

    #loop that replaces 1s with '+' and 0s with ''
    for i in range(len(newlst)):
        if newlst[i] == 1:
            display_lst.append('+')
        elif newlst[i] == 0:
            display_lst.append(' ')
    
    display_lst = str(display_lst)
    display_lst = display_lst[1:len(display_lst) - 1] #gets rid of brackets
    display_lst = display_lst.replace(',','') #replaces commas with spaces
    return display_lst
        
    
main()

