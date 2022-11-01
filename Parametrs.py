"""
Welcome to my first project. 
This project is dedicated to calculating the characteristics 
of the electrolyzer according to the specified parameters
"""
# setting the variables that we will use in the calculation
Watts_per_liter = 100
Area_per_watt = 0.1
Plates_for_two_volts = 2
Hole_deameter_per_liter = 4


def quest_and_settings():  # we ask the user what parameter he wants to set
	global User_Ans
	User_Ans = str(input(
			"Hello! \n"
			"What parameter do you want to choose to set it? "
			"\n 1 - Number plates and working area "
			"\n 2 - liters of hydrogen and Number Plates"
			"\n 3 - Watts "
			"\n 4 - Amps "
			"\n 5 - Voltage \n"
		)
	)

quest_and_settings()



def parameters_by_size():
	pass



def Print_characteristic(Watts, Number_of_liters, Working_Area, Diameter, Number_of_plates, Amps, Volts):
	print(
		"Characteristics of the electrolyzer: "
		"Electrical characteristics:"
		"\n It will be required " + str(Watts) + " watts""                   Ampere needed:" + str(Amps) +
		"\n Generate " + str(Number_of_liters) + " liters of hydrogen""      Volts needed:" + str(Volts) +
		"\n Dimensions,quantity of materials:"
		"\n Working area excluding work on both sides: " + str(Working_Area) + "m²""				    number of plates: " + str(Number_of_plates) +
		"\n Working area, considering the work on both sides: " + str(Working_Area * 2) + "m²""			Internal diameter of fittings: " + str(Diameter) +

		"\n \n \nAll parameters are relative!Use them for relative calculations, the real parameters may differ!"
		 )

def parameters_by_liters():
	Number_of_liters = float(input("How many liters of hydrogen do you want to pump out? \n"))
	Number_of_plates = int(input("how many plates do you want? \n"))
	Watts = Watts_per_liter * Number_of_liters
	Working_Area = Area_per_watt * Watts / 100
	if Number_of_liters > 1:
		Diameter = (Number_of_liters - 1) + Hole_deameter_per_liter
	elif Number_of_liters < 1:
		Diameter = Hole_deameter_per_liter * Number_of_liters
	elif Number_of_liters == 1:
		Diameter = 4
	Volts = 2 * Number_of_plates
	Amps = Watts / Volts
	Print_characteristic(Watts, Number_of_liters, Working_Area, Diameter, Number_of_plates, Amps , Volts)

def parameters_by_Watts():
	pass


def parameters_by_Amps():
	pass


def parameters_by_Volt():
	pass


# calling functions depending on the response

if User_Ans == "1":
	parameters_by_size()
	print("it Work!")
elif User_Ans == "2":
	parameters_by_liters()
elif User_Ans == "3":
	parameters_by_Watts()
elif User_Ans == "4":
	parameters_by_Amps()
elif User_Ans == "5":
	parameters_by_Volt()
else:
	print("Mistake!Try again")
	quest_and_settings()