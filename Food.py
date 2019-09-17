# Nutrition Data Collection
# By Harry Ritchie 17.09.2019

import requests # Import packages

with open('nutrition.csv', 'w') as file:

	# Write name of headers Name of food, energy value in kcal, energy per 100g, sugars value, sugars per 100g
	file.write('Name;Energy100g;Sugar100g;Fat100g;Carb100g;Weight_gram\n')
	

	for i in range(10):

		i = i * 1500 # Maximum request size per request is 1500

		url = 'http://api.nal.usda.gov/ndb/nutrients/?format=json&offset={}&max=1500&api_key=LnfwG2R9C7dQreIKKp0buDu9iCOJnwC25GYYiEJ1&nutrients=205&nutrients=204&nutrients=208&nutrients=269'.format(i + 1)
		foods = requests.get(url).json()['report']['foods']

		# For each food collect the following values
		for row in foods:

			name = row['name'] # name of food
			name = ''.join(e for e in name if e.isalnum()) # update name

			try:
				energy_per_100 = float(row['nutrients'][0]['gm']) # energy in kcal per 100 g
			except:
				energy_val = 'nan'

			try:
				sugars_per_100 = float(row['nutrients'][1]['gm']) # sugar in g per 100 g
			except:
				sugars_val = 'nan'

			try:	

				fat_per_100 = float(row['nutrients'][2]['gm']) # fat in g per 100 g

			except:
				fat_val = 'nan'

			try:

				carb_per_100 = float(row['nutrients'][3]['gm']) # cab in g per 100 g
			except:
				carb_val = 'nan'

			weight = row['weight'] # mass in g 

			file.write('{};{};{};{};{};{}\n'.format(name, energy_per_100, sugars_per_100, fat_per_100, carb_per_100, weight)) # write to file

		print("Iteration {}".format(i)) # print the iteration for each request

	file.close()

		









