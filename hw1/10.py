'''10.Write a Python program to display astrological sign for given date ofbirth.
ExpectedOutput:

Input birthday: 15
Input month of birth (e.g. march, july etc): may
Your Astrological sign is: Taurus'''

d = int(input("Input birthday: "))
m = input("Input month of birth (e.g. march, july etc): ")
if m == 'december':
	s = 'Sagittarius' if (d < 22) else 'capricorn'
elif m == 'january':
	s = 'Capricorn' if (d < 20) else 'aquarius'
elif m == 'february':
	a = 'Aquarius' if (d < 19) else 'pisces'
elif m == 'march':
	s = 'Pisces' if (d < 21) else 'aries'
elif m == 'april':
	s = 'Aries' if (d < 20) else 'taurus'
elif m == 'may':
	s = 'Taurus' if (d < 21) else 'gemini'
elif m == 'june':
	s = 'Gemini' if (d < 21) else 'cancer'
elif m == 'july':
	s = 'Cancer' if (d < 23) else 'leo'
elif m == 'august':
	s = 'Leo' if (d < 23) else 'virgo'
elif m == 'september':
	s = 'Virgo' if (d < 23) else 'libra'
elif m == 'october':
	s = 'Libra' if (d < 23) else 'scorpio'
elif m == 'november':
	s = 'scorpio' if (d < 22) else 'sagittarius'
print("Your Astrological sign is :",s)