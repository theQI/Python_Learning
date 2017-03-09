def bmrWomen (weight, heightinfeet, heightininches, age):

	result = 655 + 4.3 * w + 4.7 * ((h1 * 12) + h2) - 4.7 * a

	return result

def bmrMen (weight, heightinfeet, heightininches, age):

	result = 66 + 6.3 * w + 12.9 * ((h1 * 12) + h2) - 6.8 * a

	return result

gender = input("Are you male or female?").lower()

w = float(input("Enter your weight in pounds:"))

h1 = int(input("Enter your height in feet:"))

h2 = int(input("Enter your height in inches"))

a = float(input("Enter your age in years:"))

if gender == "male":

	BMR = bmrMen(w, h1, h2, a)

	print ("your BMR is:", " ", BMR)

if gender == "female":

	BMR = bmrWomen(w, h1, h2, a)

	print ("your BMR is:", " ", BMR)