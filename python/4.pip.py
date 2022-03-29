#라이브러리를 사용해보자 

import pandas as pd
house = pd.read_csv('boston.csv')
print(house)
print(house.head(1))
print(house.describe())

