"""
Welcome to my first project. 
This project is dedicated to calculating the characteristics 
of the electrolyzer according to the specified parameters
"""
import sys
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
			"\n 1 - liters of hydrogen and Number Plates "
			"\n 2 - Watts and Number plates \n"
		)
	)

quest_and_settings()

def Print_characteristic(Watts, Number_of_liters, Working_Area, Diameter, Number_of_plates, Amps, Volts):
	print(
		"Characteristics of the electrolyzer: "
		"\nElectrical characteristics:"
		"\n It will be required " + str(Watts) + " watts""                   Ampere needed:" + str(Amps) +
		"\n Generate " + str(Number_of_liters) + " liters of hydrogen""      Volts needed:" + str(Volts) +
		"\n Dimensions,quantity of materials:"
		"\n Working area excluding work on both sides: " + str(Working_Area) + "m²""				    number of plates: " + str(Number_of_plates) +
		"\n Working area, considering the work on both sides: " + str(Working_Area * 2) + "m²""			Internal diameter of fittings: " + str(Diameter) +

		"\n \n \nAll parameters are relative!Use them for relative calculations, the real parameters may differ!\n \n \n"
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
	new_ans = str(input("Do you want to find the parameters in a different way?"
						"\n yes or not?"
						)
				  )
	if new_ans in ("Yes", "yes", "y"):
		quest_and_settings()
	elif new_ans in ("No", "no", "n"):
		sys.exit()

def parameters_by_Watts():
	Watts = float(input("Installation power (In watts) \n"))
	Number_of_plates = int(input("how many plates do you want? \n"))
	Number_of_liters = Watts / Watts_per_liter
	Working_Area = Area_per_watt * Watts / 100
	if Number_of_liters > 1:
		Diameter = (Number_of_liters - 1) + Hole_deameter_per_liter
	elif Number_of_liters < 1:
		Diameter = Hole_deameter_per_liter * Number_of_liters
	elif Number_of_liters == 1:
		Diameter = 4
	Volts = 2 * Number_of_plates
	Amps = Watts / Volts
	Print_characteristic(Watts, Number_of_liters, Working_Area, Diameter, Number_of_plates, Amps, Volts)
	new_ans = str(input("Do you want to find the parameters in a different way?"
						"\n yes or not?"
						)
				  )
	if new_ans in ("Yes", "yes", "y"):
		quest_and_settings()
	elif new_ans in ("No", "no", "n"):
		sys.exit()



# calling functions depending on the response

if User_Ans == "1":
	parameters_by_liters()
elif User_Ans == "2":
	parameters_by_Watts()
else:
	print("Mistake!Try again")
	quest_and_settings()