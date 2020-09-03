import random

class Person:
	def __init__(self, gender):
		#if gender != "male":
		#	gender = "female"
		self.Gender = gender

	def Gender(self):
	
		return self.Gender

	def Age(self):
		age = random.randint(18,100)
		return age
	
	def foo(self):
		pass

	def FirstName(self):
		
		if self.Gender == "male":

			male_first_name = (
			"James",
			"John", 
			"Robert", 
			"Michael", 
			"William", 
			"David", 
			"Richard", 
			"Joseph", 
			"Thomas", 
			"Charles", 
			"Christopher", 
			"Daniel", 
			"Matthew", 
			"Anthony", 
			"Donald", 
			"Mark", 
			"Paul", 
			"Steven", 
			"Andrew", 
			"Kenneth"
			)

			return random.choice(male_first_name)

		else:

			female_first_name = (
			"Mary", 
			"Patricia", 
			"Jennifer", 
			"Linda", 
			"Elizabeth", 
			"Barbara", 
			"Susan", 
			"Jessica", 
			"Sarah", 
			"Karen", 
			"Nancy", 
			"Margaret", 
			"Lisa", 
			"Betty", 
			"Dorothy", 
			"Sandra", 
			"Ashley", 
			"Kimberly", 
			"Donna", 
			"Emily"
			)

			return random.choice(female_first_name)
	
	def Surname(self):
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
		bio = (
		"INSERT BIO 1",
		"INSERT BIO 2",
		"INSERT BIO 3"
		)
		return random.choice(bio)

	def Profile_Pic(self):

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

m = Person("male")
print(m.Gender)
print(m.FirstName())
print(m.Surname())
print(m.Age())
print(m.Bio())
print(m.Profile_Pic())

f = Person("female")
print(f.Gender)
print(f.FirstName())
print(f.Surname())
print(f.Age())
print(f.Bio())
print(f.Profile_Pic())