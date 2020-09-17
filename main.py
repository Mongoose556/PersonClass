from person import Person
import random

f"{name.lower()} is funny."

m = Person()
print(f"Gender: {m.gender("male")}")
print(f" Forename: {random.choice(m.male_first_name)}")
print(f"Surname: {random.choice(m.surname)}")
print(f"Age: {m.age()}")
print(f" Job: {m.bio}")
print(f"Picture: {m.profile_pic()}")
    


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