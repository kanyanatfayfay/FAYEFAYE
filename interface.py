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
    print("A:Append a value")
    print("B:Print the team")
    print("X:Exit the program")
    chioces = input("Enter your chioce")
    if choice == 'A':
        name = input("Enter a name: ")
        teamlist.append(name)
print(teamlist)