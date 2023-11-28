print("welcome to temperature converter, a lightweight utility for converting temperatures")

#create variables for the unit that is being converted and the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))

#function that converts C to F
def c_to_f(temp_c):
    converted_c = temp_c * (9/5) + 32
    return converted_c

#function that converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f - 32) * (5/9)
    return converted_f

#function that converts K to F
def k_to_f(temp_k):
    converted_k = (temp_k - 273.15) * (9/5) + 32
    return converted_k

#function that converts F to K
def f_to_k(temp_fk):
    converted_fk = (temp_fk - 32) * (5/9) + 273.15 
    return converted_fk

#main function that uses conditionals to decide which convert function to select
def main():
    if(unit == "C"):
        celsius_to_fahrenheit = c_to_f(value)
        return celsius_to_fahrenheit
    elif(unit == "F"):
        fahrenheit_to_celsius = f_to_c(value)
        return fahrenheit_to_celsius
    elif(unit == "K"):
        kelvin_to_fahrenheit = k_to_f(value)
        return kelvin_to_fahrenheit
    elif(unit == "FK"):
        fahrenheit_to_kelvin = f_to_k(value)
        return fahrenheit_to_kelvin
    else:
        warning = "Please enter C, F, K, or FK to specify the unit: "
        return warning


#print results
result = main()
print("Your value is: " + str(result))