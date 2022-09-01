it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Length of the set it_companies
print("Length of the set:")
print(len(it_companies))

#Adding 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Inserting multiple IT companies at once to the set it_companies
it_companies.add("Yahoo")
it_companies.add("Sony")
it_companies.add("Hewlett & Packard")
print(it_companies)

#Removing IBM from the set it_companies
it_companies.remove("IBM")
print(it_companies)

#Difference between remove and discard
print("Remove can cause a KeyError exception, while Discard does not.")

#Joining A and B
C = A | B
print(C)

#Finding intersection of A and B
D = A & B
print(D)

#Is A subset of B
print("Yes because all A's values are part of B.")
###
#Are A and B disjoint sets
print("No because they contain shared values.")
###
#Joining A with B and B with A
E = A | B
F = B | A
print(E)
print(F)

#Symmetric difference between A and B
G = B - A
print(G)

#Deleting the sets completely
A.clear()
B.clear()
print(A)
print(B)

#Converting the ages to a set and comparing the length of the list and the set.
ageset = set(age)
print(len(age))
print(len(ageset))