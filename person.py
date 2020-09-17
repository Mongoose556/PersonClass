import random
import json
import logging

logging.basicConfig(filename="person.log", level=logging.INFO, format='%(levelname)s:%(message)s')

#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# TODO: make attributes assignable, e.g. .Age = 25, Name = dave etc 
# TODO: read names etc from a file
# TODO: age missing from output

class Person:
	""" Creates an instance of the Person class, 
	Reads the data files """

	def __init__(self):

		#read name files and log errors
		from pathlib import Path

		if not Path("data/female_names.json").is_file():
			logging.info("Could not find file! data/female_names.json")
			raise ValueError(f"Could not find file! data/female_names.json")

		# Male
		if not Path("data/male_names.json").is_file():
			logging.info("Could not find file! data/male_names.json")
			raise ValueError(f"Could not find file! data/male_names.json")
			
		# Surnames
		if not Path("data/surnames.json").is_file():
			logging.info("Could not find file! data/surnames.json")
			raise ValueError(f"Could not find file! surnames.json")
			
		# Bio's
		if not Path("data/bio.json").is_file():
			logging.info("Could not find file! data/bio.json")
			raise ValueError(f"Could not find file! bio.json")
			
		# assign data
		# male names
		with open("data/male_names.json", 'r') as json_file:
			data = json.load(json_file)
			self.male_first_name = data['male_forenames']

		# female names
		with open("data/female_names.json", 'r') as json_file:
			data = json.load(json_file)
			self.female_first_name = data['female_forenames']

		# surnames
		with open("data/surnames.json", 'r') as json_file:
			data = json.load(json_file)
			self.surname = data['surnames']

		# bio's
		with open("data/bio.json", 'r') as json_file:
			data = json.load(json_file)
			self.bio = data['jobs']

### ### Main Methods ### ### 

	def male_first_name(self, forename=""):
		""" Returns a random male name """
		if forename == None:
			return random.choice(self.male_first_name())
		else:
			return forename

	def female_first_name(self, forename=""):
		""" Returns a random female name """
		if forename == None:
			return random.choice(self.female_first_name())
		else:
			return forename
	
	def surname(self, surname=""):
		""" Returns a random surname """
		if surname == None:
			return random.choice(self.surname())
		else:
			return surname

	def gender(self, gender):
		""" Assigns or returns a gender (str) """
		if gender == None:
			self.gender = random.choice("male", "female")
		else:
			self.gender = gender
		return self.gender

	def age(self, age=None):
		""" Generates a random age 16 - 100 if none supplied """
		if age == None:
			self.age = random.randint(16,110)
		else:
			self.age = age
		return self.age

	def bio(self, bio=""):
		if bio == None:
			return random.choice(self.bio())
		else:
			return bio

	def create_random(self):
		""" Returns a tuple: Gender, Firstname, Lastname, Age, Bio, Picture """
		sex = ("male", "female")
		g = random.choice(sex)

		if g == "male":
			fn = self.male_first_name()
		else:
			fn = self.female_first_name()

		self.gender = g
		a = self.age()
		sn = self.surname()
		b = self.bio()
		pf = self.profile_pic()
		# return as dict?

		return (g, fn, sn, a, b, pf) #tuple

	def profile_pic(self):
		""" Returns a random picture """
		if self.gender == "male":

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