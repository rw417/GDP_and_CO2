import pandas as pd


data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

mort_rate = data['Mortality rate, infant (per 1,000 live births)']
gdp_percap = data['GDP per capita (constant 2010 US$)']
country = data['Country Nameg']