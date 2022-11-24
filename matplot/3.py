import matplotlib.pyplot as plt, numpy as np 
countries = { 
    "China": 1_439_323_776, "India": 1_380_004_385, "USA": 331_002_651, "Indonesia": 273_523_615, "Pakistan": 220_892_340,  
    "Brazil": 212_559_417, "Russia": 145_934_462, "Japan": 126_476_461, "Turkey": 84_339_067, "France": 65_273_511 
} 
myexplode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
plt.title("Population Dencity Index") 
plt.pie(countries.values(), labels = countries.keys(), explode = myexplode, autopct='%1.1f%%', shadow = True) 
plt.show()