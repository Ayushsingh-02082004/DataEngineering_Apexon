import math

t = float(input("Enter temperature in farenheit : "))
v = float(input("Enter wind speed : "))

wind_chill = 35.74 + 0.6215*t + (0.4275*t - 35.75) * math.pow(v, 0.16)

print("Wind Chill" , wind_chill)