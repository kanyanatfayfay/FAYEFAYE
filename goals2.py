#create an empty list
goals = []

#append the goals
n = int(input("How many goals do you want? "))
for i in range(n):
    new = input('Add the new goal to the lists: ')
    goals.append(new)

print(goals)
#edit an item
i = input('which goal do you want to change? ')
#convert i string to the integer
i = int(i)
goals[i-1] = input('Enter a new goal: ')

print(goals)

#delete an item
i = int(input ('Which goals do you want to delete? '))
del goals[i-1]
print(goals)