def finalHeight(heightInFeet,heightInInch):
    finalHeight=heightInFeet*12+heightInInch
    return finalHeight

def bmrMen(age,weight,finalHeight):
    bmrMen=66+(6.3*weight)+(12.9*finalHeight)-(6.8*age)
    return bmrMen

def bmrWomen(age,weight,finalHeight):
    bmrWomen=655+(4.3*weight)+(4.7*finalHeight)-(4.7*age)
    return bmrWomen

print("Welcome to the BMR calculating machine")
age=float(input("Enter your age"))
weight=float(input("Enter your weight"))
print("Enter you height in in format feet and inch")
heightInFeet=float(input("feet"))
heightInInch=float(input("inch"))

resultOfHeight=finalHeight(heightInFeet,heightInInch)


gender=input("Enter m for male and f for female")
if gender=="m":
    resultOfMen=bmrMen(age,weight,resultOfHeight)
    print("Your BMR is:", resultOfMen)
elif gender=="f":
    resultOfWomen=bmrWomen(age,weight,resultOfHeight)
    print("Your BMR is:", resultOfWomen)