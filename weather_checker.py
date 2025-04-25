print("Weather Checher")
temperature = float(input("what is the temperature today? °C: "))
if temperature > 30:
    print("it's hot, stay hydrated. ")
elif temperature > 20:
    print("its warm and nice outside. ")
elif temperature > 10:
    print("its cold outside, grab a jacket. ")
else:
    print("its freezing grab a jacket, make hot choco")
