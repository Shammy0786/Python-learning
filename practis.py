i = int(input("Enter age or year of birth \n"))

if i<100:
    print(f"You enter age {i} \n year of birth is {2021-i}")

elif 100<i<200:
    print("You seem like old one")

elif 1800<i<2021:
    print(f"You Enter year of birth {i} \n Your age is {2021-i}")


yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

