import numpy as np
import datetime
import pandas as pd





class electricity_consumption:

	"""Simulating electricity data"""

	def __init__(self):

		self.dates = []
		self.weekend = [5,6]
		self.summer_months = [4,5,6,7,8]
		self.summer_pers = np.arange(10,20)
		self.winter_pers = np.arange(8,18)

	def generateDates(self):

		dt = datetime.datetime(2019, 3, 15,18)
		end = datetime.datetime(2021, 3, 15,18)
		step = datetime.timedelta(hours=24)

		dates = []

		while dt < end:
		    dates.append(dt.strftime('%Y-%m-%d %H:%M'))
		    dt += step

		return dates

	def genratingData(self,initial_reading):
		
		dates = self.generateDates()
		print(dates)
		consumption_dict = {}
		for date in dates:
		    stripped = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
		    day = stripped.weekday()
		    month = stripped.month
		    if month in self.summer_months:
		        if day in self.weekend:
		            # Make each of the last 5 elements 5x more likely
		            prob = [1.0]*(len(self.summer_pers)-5) + [5.0]*5

		            # Normalising to 1.0
		            prob /= np.sum(prob)
		            day_consumption  = np.random.choice(self.summer_pers, p = prob)
		        else:

		            day_consumption  = np.random.choice(self.summer_pers)
		    else:
		        if day in self.weekend:
		            
		            # Make each of the last 5 elements 5x more likely
		            prob = [1.0]*(len(self.winter_pers)-5) + [5.0]*5

		            # Normalising to 1.0
		            prob /= np.sum(prob)
		            day_consumption  = np.random.choice(self.winter_pers, p = prob)

		        else:

		            day_consumption  = np.random.choice(self.winter_pers)


		    initial_reading += day_consumption


		    consumption_dict[date] = initial_reading

		#Generating some laplace noise to add to the data
		noise = np.random.laplace(loc=0, scale=1, size=len(consumption_dict)) 

		df = pd.DataFrame(consumption_dict.items(), columns=['date', 'electricity_consumption'])
		df['electricity_consumption'] = df['electricity_consumption'] + noise


		return df

if __name__ == '__main__':

	data = electricity_consumption()
	d = data.genratingData(10)
	print(d.head())
	