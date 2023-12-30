# 1 ℃ = (1 ℉ -32)/1.8
# 1 ℉ = (1 ℃ x 1.8) + 32
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit -32)/1.8
    return  celsius