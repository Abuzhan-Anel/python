import pandas as pd
import numpy as np
data = pd.read_csv('BigmacPrice.csv')
data_name= data.set_index('name')
data_date= data.set_index('date')
data_currency_code= data.set_index('currency_code')
print(data[data['dollar_price'] > 3])
