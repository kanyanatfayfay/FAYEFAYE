#Program interface should have all  of these:
#1.tell the user ahat the program is and what is can do.
#2.tell the user make chioces or select option
#3.let the user enter information - you as a delverloper should include a helpful massage
#4.for every inter face displayresult or answer
#5.make the user close the program

teamlist = []
choice = ' ' 
while choice != 'X':
    print("TEAM MANAGER")
    print("============")
    print("This program will help you manager your team")
    print("\n")
    print("A: Append a value")
    print("B: Print the team")
    print("C: Print an element")
    print("D: Delete an element")
    print("E: Edit an element")
    print("F: Sort the list")
    print("X: Exit the program")
    chioces = input("Enter your chioce: ")
    if choice == "A":
        name = input("Enter a name: ")
        teamlist.append(name)
    if choice == "B":
        print(teamlist)
    if choice == "C":
        i = input("Which list item do you want?: ")
        i = int(i)
        print(teamlist[i])
    if choice == "D":
        i = int(input("Which item do you want to detele?: "))
        del(teamlist[i])
    if choice == "E":
        i = int(input("Which list item do you want to edit?: "))
        teamlist[i-1] = input("Enter the new name: ")
        print(teamlist)
    if choice == "F":
        teamlist.sort()       