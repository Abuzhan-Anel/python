'''5.Write a Python program to convert month name to a number of days.
ExpectedOutput:List of months: January, February, March, April,May, June, July, August, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days'''

mon= input('name of Month: ')
months= ["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November", "December"]
if (mon == "February"):
    print("Num of days: 28/29 days")
elif mon in ("January" , "March" ,"May" , "July" , "August" , "October" ,  "December"):
    print("Num of days: 31 days")
elif mon in ( "February" , "April" , "June" , "September" , "November" ):
    print("Num of days: 30 days")
else :
    print("wrong")
