#tuple containing names of your sisters and your brothers
brothers = ("Jim", "Omarion")
print("brothers")
print(brothers)
sisters = ("Megan", "Natasha")
print("sisters")
print(sisters)

#Joining brothers and sisters tuples and assigning them to siblings
siblings = brothers + sisters
print("siblings")
print(siblings)

#Counting number of siblings
print("My siblings are")
print(len(siblings))

#adding the name of my father and mother and assigning it to family_members
family_members = siblings + ("Gurmit", "Tina")
print("All family members' names")
print(family_members)