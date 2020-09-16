import random
import json

#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# TODO: make attributes assignable, e.g. .Age = 25, Name = dave etc 
# TODO: read names etc from a file?
# TODO: age missing from output

class Person:
	""" Creates an instance of the Person class """

	def __init__(self):
		#read name files
		from pathlib import Path

		if not Path("female_names.json").is_file():
			raise ValueError(f"Could not find file! female_names.json")

		if not Path("male_names.json").is_file():
			raise ValueError(f"Could not find file! male_names.json")

		if not Path("surnames.json").is_file():
			raise ValueError(f"Could not find file! surnames.json")

		if not Path("bio.json").is_file():
			raise ValueError(f"Could not find file! bio.json")

		# male names
		with open("male_names.json", 'r') as json_file:
			male = {}
			male = json.load(json_file)
			self.Male_First_Name = male['male_forenames']

		# female names
		with open("female_names.json", 'r') as json_file:
			female = json.load(json_file)
			self.Female_First_Name = female['female_forenames']

		# surnames
		with open("surnames.json", 'r') as json_file:
			surname = json.load(json_file)
			self.Surname =surname['surnames']

	def Male_First_Name(self, forename=""):
		""" Returns a random male name """
		if forename == None:
			return random.choice(self.Male_First_Name())
		else:
			return forename

	def Female_First_Name(self, forename=""):
		""" Returns a random female name """
		if forename == None:
			return random.choice(self.Female_First_Name())
		else:
			return forename
	
	def Surname(self, surname=""):
		""" Returns a random surname """
		if forename == None:
			return random.choice(self.Surname())
		else:
			return surname
	

	def Bio_File(self, filename="bio.json"):
		pass

	def Create_Random(self):
		""" Returns a tuple: Gender, Firstname, Lastname, Age, Bio, Picture """
		sex = ("male", "female")
		g = random.choice(sex)

		if g == "male":
			fn = self.Male_First_Name()
		else:
			fn = self.Female_First_Name()

		self.Gender = g
		a = self.Age()
		sn = self.Surname()
		b = self.Bio()
		pf = self.Profile_Pic()
		# return as dict?

		return (g, fn, sn, a, b, pf) #tuple

	def Gender(self, gender):
		""" Assigns or returns a gender (str) """
		self.Gender = gender
		return self.Gender

	def Age(self, age=None):
		""" Generates a random age 18- 100 """
		if age == None:
			a = random.randint(0,110)
		else:
			a = age
		return a

	def Bio(self):
		""" Returns a random bio """
		bio = (
		"Toilet Cleaner",
		"Head Pooper",
		"Nappy Licker",
		"Ear chewer",
		"Eye Licker",
		"House Smoosher",
		"Fart Smeller"
		)
		return random.choice(bio)

	def Profile_Pic(self):
		""" Returns a random picture """
		if self.Gender == "male":

			male_picture = (
				"male_pic1.jpg",
				"male_pic2.jpg",
				"male_pic3.jpg"
				)
			return random.choice(male_picture)
		else:
			female_picture = (
				"female_pic1.jpg",
				"female_pic2.jpg",
				"female_pic3.jpg"
			)
		return random.choice(female_picture)
	
m = Person()
print(m.Gender("male"))
print(random.choice(m.Male_First_Name))
print(random.choice(m.Surname))
print(m.Age())
print(m.Bio())
print(m.Profile_Pic())

'''
f = Person()
print(f.Gender)
print(f.Female_First_Name())
print(f.Surname())
print(f.Age())
print(f.Bio())
print(f.ProfilePic())

'''

#p = Person()
#r = p.Male_First_Name()
#print(r)