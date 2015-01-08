#!/usr/local/bin/python3
# Joseph Urbanski
# jurbanski@ci.uchicago.edu
# 2014-01-08

tempF = eval(input("Please input the temperature in Fahrenheit you want converted to Celcius:\n"))
tempC = (tempF - 32) * 5 / 9
print("Temperature in Celcius:", round(tempC, 1))
