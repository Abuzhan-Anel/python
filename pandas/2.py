import pandas as pd
import numpy as np
data = pd.read_csv('BigmacPrice.csv')
print(len(data['name'].unique()))

