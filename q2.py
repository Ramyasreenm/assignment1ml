# Empty Dictionary
dog = {}
#print dictionary
print(dog)

#Adding name, color, breed, legs, age to the dog dictionary
dog['name'] = '29'
dog['color'] = '28'
dog['breed'] = '27'
dog['legs'] = '26'
dog['age'] = '25'
print(dog)

#student dictionary with first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 't'
student['last_name'] = 'g'
student['gender'] = 'j'
student['age'] = 'k'
student['marital_status'] = 'l'
student['skills'] = ['a','b']
student['country'] = 'x'
student['city'] = 'h'
student['address'] = 'r'
print(student)

#length of the student dictionary
print('Student Dictionary length')
print(len(student))

print("value of skills and the data type, as a list")
print(type(student['skills']))

#adding skills values by adding one or two skills
print("adding skills values by adding skills")
student['skills'].append('f1')
student['skills'].append('g1')
print(student['skills'])

#Dictionary keys as a list
print(student.keys())
#Dictionary values as a list
print(student.values())