# === Part 1: Sorting List for Min Age ===
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

minages = min(ages)

print("The Minimum age is:",minages)

#===Sorting List for Max Age===
maxages = max(ages)

print("The Maximum age is:",maxages)

# ===Part 2: Adding the min age and the max age again to the list ===
print("Adding max and min ages to list")
ages.insert(0, 19)
ages.insert(11, 26)
print(ages)

# === Part 3: Finding the median age (one middle item or two middle items divided by two)
print("Median Age is:",(ages[6]-ages[5])/2+ages[5])

# === Part 4: Finding the average age (sum of all items divided by their number)
print("The Average age is",sum(ages)/len(ages))

# === Part 5:  Find the range of the ages (max minus min)
print("Range of ages is",ages[11]-ages[0])
