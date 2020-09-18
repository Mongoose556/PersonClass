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
			raise ValueError(f"Could not find file! data/surnames.json")
			
		# job's
		if not Path("data/jobs.json").is_file():
			logging.info("Could not find file! data/jobs.json")
			raise ValueError(f"Could not find file! data/jobs.json")
			
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

		# job's
		with open("data/jobs.json", 'r') as json_file:
			data = json.load(json_file)
			self.job = data['occupations']

### ### Main Methods ### ### 

	def male_first_name(self, forename=""):
		""" Returns a dictionary of names or accepts a variable """
		self.male_first_name = forename
		return self.male_first_name


	def female_first_name(self, forename=""):
		""" Returns a dictionary of names or accepts a variable """
		self.female_first_name = forename
		return self.female_first_name
	

	def surname(self, surname=""):
		""" Returns a dictionary of surnames or accepts a string """
		self.female_first_name = surname
		return self.surname


	def gender(self, gender=None):
		""" Assigns or returns a gender (str) """
		if gender == None:
			self.gender = random.choice(["male", "female"])
		else:
			self.gender = gender
		return self.gender


	def age(self, age=None):
		# TODO: Accept only INT
		""" Generates a random age 16 - 100 if none supplied """
		if age == None:
			self.age = random.randint(16,110)
		else:
			self.age = age
		return self.age


	def job(self, job=""):
		self.job = job
		return self.job


	def create_random(self):
		""" Returns a tuple: Gender, Firstname, Lastname, Age, job, Picture """
		g = self.gender()

		if g == "male":
			firstname = random.choice(self.male_first_name)
		else:
			firstname = random.choice(self.female_first_name)

		a = self.age()
		surname = random.choice(self.surname)
		job = random.choice(self.job)
		pic = self.profile_pic()
		# return as dict?

		x = ()

		x = (g, firstname, surname, a, job, pic)

		return x


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