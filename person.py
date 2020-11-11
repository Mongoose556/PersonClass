import random
import json
import logging

logging.basicConfig(filename="person.log", level=logging.INFO, format='%(levelname)s:%(message)s')

#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

class Person:
	""" Creates an instance of the Person class, reads the data files """

	def __init__(self):
		# TODO: Is there a better way of doing this? Try / Except?
		#read name files and log errors
		from pathlib import Path

		# Female
		filename = "data/female_names.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")


		with open("data/female_names.json", 'r') as json_file:
			data = json.load(json_file)
			self.female_first_name = data['female_forenames']
		###

		# Male
		filename = "data/male_names.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")

		with open(filename, 'r') as json_file:
			data = json.load(json_file)
			self.male_first_name = data['male_forenames']

		# Surnames
		filename = "data/surnames.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")

		with open(filename, 'r') as json_file:
			data = json.load(json_file)
			self.surname = data['surnames']
		
		# jobs
		filename = "data/jobs.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")


		with open("data/jobs.json", 'r') as json_file:
			data = json.load(json_file)
			self.job = data['occupations']

		# Bio
		filename = "data/bio.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")

		with open(filename, 'r') as json_file:
			data = json.load(json_file)
			self.bio = data['info']

		# female pictures
		filename = "data/female_pics.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")

		with open(filename, 'r') as json_file:
			data = json.load(json_file)
			self.female_profile_pic = data['pictures']

		# male pictures
		filename = "data/male_pics.json"
		if not Path(filename).is_file():
			logging.info(f"Could not find file! {filename}")
			raise ValueError(f"Could not find file! {filename}")

		with open(filename, 'r') as json_file:
			data = json.load(json_file)
			self.male_profile_pic = data['pictures']


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
		""" Assigns or returns a gender (str), if None provided then random choice Male/Female """
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
		""" Assigns a job or returns a list of jobs """
		self.job = job
		return self.job

	def create_random(self):
		""" Returns a tuple: Gender, Firstname, Lastname, Age, job, Picture """
		gender = self.gender()

		if gender == "male":
			firstname = random.choice(self.male_first_name)
			pic = random.choice(self.male_profile_pic)
		else:
			firstname = random.choice(self.female_first_name)
			pic = random.choice(self.male_profile_pic)

		age = self.age()
		#birth_year = self.year_of_birth()
		surname = random.choice(self.surname)
		job = random.choice(self.job)

		x = ()

		x = (gender, firstname, surname, age, job, pic)

		return x

	def female_profile_pic(self):
		""" Returns a list of pictures """
		return self.female_profile_pic

	def male_profile_pic(self):
		""" Returns a list of pictures """
		return self.male_profile_pic
	
	'''
	def year_of_birth(self):
		import datetime
		today = datetime()
		year = today.datetime.today
		yob = year - self.age
		return yob

	'''