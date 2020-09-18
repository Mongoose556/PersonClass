from person import Person
import random

p = Person()
'''
print(f"Gender: {p.gender()}")

if p.gender == "male":
    print(f"Forename: {random.choice(p.male_first_name)}")
else:
    print(f"Forename: {random.choice(p.female_first_name)} {random.choice(p.surname)}")

print(f"Age: {p.age()}")
print(f"    Job: {random.choice(p.job)}")

#print(f"Picture: {p.profile_pic()}")
'''
x = p.create_random()

print(x)


'''
f = Person()
print(f.Gender)
print(f.Female_First_Name())
print(f.Surname())
print(f.Age())
print(f.Bio())
print(f.ProfilePic())


p = Person()
r = p.Male_First_Name()
print(r)

'''