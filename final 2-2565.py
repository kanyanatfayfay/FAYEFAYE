cities = ["Suphanburi", "Bangkok", "Chiang mai", "Chiangrai", "Prachuap Khiri Khan"]

for i in range(len(cities)):
    print(cities[i])

name = input("Enter a new city to add to the list: ")
cities.append(name)

delete = int(input("Enter the index of a city to delete from the list: "))
del cities[delete]

print(cities)