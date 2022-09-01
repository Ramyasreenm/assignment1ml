#Program that reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop.
N = float(input("Please Enter number of students: "))
studs = 1
weights = []
while studs <= N:
    studs1 = float(input("Enter student "+str(studs)+"'s weight: "))
    studs2 = studs1 * 0.45359237
    weights.insert(studs, studs2)
    studs += 1
print("Students' weigts:",weights)