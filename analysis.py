import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

mort_rate = data['Mortality rate, infant (per 1,000 live births)']
gdp_percap = data['GDP per capita (constant 2010 US$)']
country = data['Country Name']

plt.scatter(y=mort_rate, x=gdp_percap, alpha=0.5)
plt.ylabel("Mortality rate, infant (per 1,000 live births)")
plt.xlabel("GDP per capita (constant 2010 US$)")
plt.title("Infant Mortality Rate vs GDP per Capita")
plt.show()

