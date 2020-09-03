import random

class Spouse:
	def __init__(self, gender="male"):
		self.Gender = gender

	def Gender(self):
	
		return self.Gender

	def Age(self):
		age = random.randint(18,100)
		return age

	def MaleFirstName(self):

		spouse_male_first_name = (
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
		return random.choice(spouse_male_first_name)

	def FemaleFirstName(self):
			spouse_female_first_name = (
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
			return random.choice(spouse_female_first_name)
	
	def Surname(self):
		spouse_surname = (
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

		return random.choice(spouse_surname)

	def Spouse_Bio(self):
		bio = (
		"INSERT BIO 1",
		"INSERT BIO 2",
		"INSERT BIO 3"
		)
		return random.choice(bio)

	def Profile_Pic(self):

		if Spouse.Gender == "male":
			male_picture = (
				"male_pic1.jpg"
				)
			return random.choice(male_picture)
		else:
			female_picture = (
				"female_pic1.jpg"
			)
		return random.choice(female_picture)

s = Spouse("female")
print(s.Gender)
print(s.FemaleFirstName())
print(s.Surname())
print(s.Age())
print(s.Spouse_Bio())
print(s.Profile_Pic())
