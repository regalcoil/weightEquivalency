options = ['grains    ', 'drams     ', 'ounces    ', 'pounds    ', 'kilograms ', 'gross tons']
symbols = ['g', 'amd', 'oz', 'lbs', 'kg', 'tons']
relative = [1, 27.3438, 437.5008, 7000.0128, 15432.368219136, 15680028.672]
print(" ")
print("Please select an option")
print(" ")
counter = 0
counter2 = 0
while counter < len(options):
	print(str(counter+1) + ": " + options[counter])
	counter = counter+1
print(" ")
choice = int(input()) - 1
print(" ")
print("Please enter an amount")
print(" ")
choice2 = float(input())
print(" ")
while counter2 < len(options):
	equivalency = choice2*(relative[choice]/relative[counter2])
	equivalency = round(equivalency, 3)
	print(options[counter2] + ": " + str(equivalency) + " " + symbols[counter2])
	counter2 = counter2+1