"""
Welcome to my first project. 
This project is dedicated to calculating the characteristics 
of the electrolyzer according to the specified parameters
"""

def quest_and_settings():			#we ask the user what parameter he wants to set
	 global User_Ans
	 User_Ans = int(input(
						"Hello! \n"
						"What parameter do you want to choose to set it? "
						"\n 1 - Size "
						"\n 2 - liters of hydrogen"
						"\n 3 - Watts "
						"\n 4 - Amps "
						"\n 5 - Voltage \n"
	 					))
quest_and_settings()

def parameters_by_size():
	pass

def parameters_by_liters():
	pass

def parameters_by_Watts():
	pass

def parameters_by_Amps():
	pass

def parameters_by_Volt():
	pass

#calling functions depending on the response

if (User_Ans == 1):
	parameters_by_size()
	print("it Work!")
elif(User_Ans == 2):
	parameters_by_liters()
elif(User_Ans == 3):
	parameters_by_Watts()
elif(User_Ans == 4):
	parameters_by_Amps()
elif(User_Ans == 5):
	parameters_by_Volt()
else:
	print("Mistake!Try again")