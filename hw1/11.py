'''Write a Python program to display the sign ofthe Chinese Zodiac forgiven year in which you were born.
ExpectedOutput:
Input your birth year: 1986
Your Zodiac sign: Tiger'''

y = int(input("Input your birth year: "))
x= y -1900

if x % 12 == 0 :
    print("Your Zodiac sign: Rat ")
elif x %12 == 1 :
    print("Your Zodiac sign: Ox ")
elif x %12 ==2:
    print("Your Zodiac sign: Tigger ")
elif x %12 ==3:
    print("Your Zodiac sign: Rabbit ")
elif x %12 ==4 :
    print("Your Zodiac sign: Dragon ")
elif x %12 ==5:
    print("Your Zodiac sign: Snace ")
elif x %12 ==6:
    print("Your Zodiac sign: Horse ")
elif  x %12 == 7:
    print("Your Zodiac sign: Goat ")
elif x %12 == 8:
    print("Your Zodiac sign: Monkey ")
elif x %12 == 9:
    print("Your Zodiac sign: Rooster ")
elif x %12 == 10:
    print("Your Zodiac sign: Dog ")
elif x %12 == 11:
    print("Your Zodiac sign: Pig ")