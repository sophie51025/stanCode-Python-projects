"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop asking new number
EXIT = -100


def main():
	"""
	When scientist keys in temperature, the app is able to provide average, highest, lowest, cold days info back to user.
	"""
	print('stanCode Master \"Weather master 4.0" !')
	print('Key in ' + str(EXIT) + ' to stop')
	weather = int(input('Daily Temperature:'))
	if weather == EXIT:
		print('No temperature was entered')
	else:
		lowest = weather
		highest = weather
		# sum_ record: to add up all weather record
		sum_record = weather
		# count: to count how many numbers are keyed in for average
		count = 1
		average = weather / count
		if weather < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			weather = int(input('Daily Temperature:'))
			if weather == EXIT:
				break
			else:

				if weather < lowest:
					lowest = weather
				if weather > highest:
					highest = weather
				if weather < 16:
					cold_day += 1
				sum_record += weather
				count += 1
				average = sum_record / count

		print('The highest temperature is ' + str(highest))
		print('The lowest temperature is ' + str(lowest))
		print('Average temperature is ' + str(average))
		print(str(cold_day) + ' cold day(s)')
		print('Total temperature entered: ' + str(count))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
