football_team = []

#TO-DO:append 11 players name
for i in range(11):
    name = input("Add a player to the football team: ")
    football_team.append(name)
    print(football_team)

#TO-DO:edit an item.    [Me;(9-11)"this is QUESTION"]
#TO-DO:delete an item.
#Ask user which item to change/delete.
repeat = 'Y'
while repeat == 'Y':  
    edit = int(input("Which players do you want to change?: ")) 
    football_team[edit-1] = input("Edit the new player: ")
    print(football_team)

    delete = int(input("Which player do you want to delete?: "))
    del football_team[delete-1]
    print(football_team)

   repeat=("Do you want to edit or delete name(Y/N) ")