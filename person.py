import random
import json

#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# TODO: make attributes assignable, e.g. .Age = 25, Name = dave etc 
# TODO: read names etc from a file?
# TODO: age missing from output

class Person:
	""" Creates an instance of the Person class """

	def __init__(self):
		pass

	def Bio_File(self, filename="bio.txt"):
		pass

	def Forename_File(self, filename="forenames.txt"):
		pass

	def Surname_File(self, filename="surname.json"):
		pass

	def Create_Random(self):
		""" Returns a tuple: Gender, Firstname, Lastname, Age, Bio, Picture """
		sex = ("male", "female")
		g = random.choice(sex)
		self.Gender = g
		a = self.Age()
		fn = self.First_Name()
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

	def First_Name(self, filename="/forenames.txt"):

		""" Returns a random name dependent on Gender """
		
		""" Read a file to import names """

		# read file
		# parse forenames dictionary, key - names

		if self.Gender == "male":

			with open(filename) as json_file:
				forename = json.load(json_file)
				for p in forename['male_forenames']:
					return random.choice(forename['name'])

		else:
			with open(filename) as json_file:
				forename = json.load(json_file)
				for p in forename['female_forenames']:
					return random.choice(forename['name'])
	
	def Surname(self):
		""" Returns a random surname """
		surname = (
			"Smith",
			"Jones",
			"Black",
			"White",
			"Anderson",
			"Bates",
			"Clark",
			"Davis",
			"Easton",
			"Johnson",
			"Williams",
			"Jones",
			"Brown",
			"Miller",
			"Wilson",
			"Moore",
			"Taylor",
			"Thomas",
			"Jackson",
			"Harris",
			"Martin",
			"Thompson",
			"Garcia",
			"Martinez",
			"Robinson"
		)

		return random.choice(surname)

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
'''		
m = Person()
print(m.Gender)
print(m.FirstName())
print(m.Surname())
print(m.Age())
print(m.Bio())
print(m.ProfilePic())

f = Person()
print(f.Gender)
print(f.FirstName())
print(f.Surname())
print(f.Age())
print(f.Bio())
print(f.ProfilePic())
'''

p = Person()
r = p.Create_Random()
print(r)