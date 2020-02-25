
# Add Details about this repository

This repository contains the experimental data downloaded from UCI machine learnning repository. The data was recorded during the experiments performed for the analysis of power consumption of various appliances by the University of Mans, Belgium. The University of Mans holds all the rights to this dataset, I downloaded this dataset from official UCI repository for my own project, to create a machine learning model for predicting the appliances energy consumption.

`Link for dataset` : 


This repository is the result of my personal interest to understand the principles and implementation of machine learning algorithms and predictive models.

`energydata_complete.csv` :: Contains the recorded data from the experiment

`DataDriven_Model.ipynb` :: Is the implementation file (jupyter notebook) containing the regression model that was used to make predictions about the comsumption of power by appliances.


# About the data

This data set contains experimental data recoded during the experiments performed to analyse appliances energy use in a low energy building. The were experiments performed by University in Mons, Belgium and they own all rights to this datas set.

Data used include measurements of temperature and humidity sensors from a wireless network, weather from
a nearby airport station and recorded energy use of lighting fixtures. The data was recorded at every 10 minutes fro about 4.5 months. The house temperature and humidity conditions were monitored with a ZigBee wireless sensor network. Each wireless node transmitted the temperature and humidity conditions around 3.3 minutes. Then, the wireless data was averaged for 10 minutes periods. The energy data was logged every 10 minutes. Weather from the nearest airport weather station (Chievres Airport, Belgium) was downloaded from a public data set from Reliable Prognosis (rp5.ru), and merged together with the experimental data sets using the date and time column. Two random variables have been included in the data set for testing the regression models and to filter out non predictive attributes (parameters).


The columns in this data set are in form of nomenclatures and the details of each are as follows:

1. date time year-month-day hour:minute:second
2. Appliances, energy use in Wh
3. lights, energy use of light fixtures in the house in Wh
4. T1, Temperature in kitchen area, in Celsius
5. RH_1, Humidity in kitchen area, in percentage
6. T2, Temperature in living room area, in Celsius
7. RH_2, Humidity in living room area, in percentage
8. T3, Temperature in laundry room area
9. RH_3, Humidity in laundry room area, in percentage
10. T4, Temperature in office room, in Celsius
11. RH_4, Humidity in office room, in percentage
12. T5, Temperature in bathroom, in Celsius
13. RH_5, Humidity in bathroom, in percentage
14. T6, Temperature outside the building (north side), in Celsius
15. RH_6, Humidity outside the building (north side), in percentage
16. T7, Temperature in ironing room , in Celsius
17. RH_7, Humidity in ironing room, in percentage
18. T8, Temperature in teenager room 2, in Celsius
19. RH_8, Humidity in teenager room 2, in percentage
20. T9, Temperature in parents room, in Celsius
21. RH_9, Humidity in parents room, in percentage
22. T_out, Temperature outside (from Chievres weather station), in Celsius
23. Pressure (from Chievres weather station), in mm Hg
24. RH_out, Humidity outside (from Chievres weather station), in percentage
25. Wind speed (from Chievres weather station), in m/s
26. Visibility (from Chievres weather station), in km
27. Tdewpoint (from Chievres weather station), Â°C
28. rv1, Random variable 1, nondimensional
29. rv2, Random variable 2, nondimensional

For more information about the data collection, scripts and figures, please refer to the paper :
Luis M. Candanedo, Veronique Feldheim, Dominique Deramaix, Data driven prediction models of energy use of appliances in a low-energy house, Energy and Buildings, Volume 140, 1 April 2017, Pages 81-97, ISSN 0378-7788
