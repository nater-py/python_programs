# Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.

# It should then return c_temp.

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Testing f_to_c function

f100_in_celsius = f_to_c(100)

# Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

# It should then return f_temp.

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32

# Testing c_to_f function

c0_in_fahrenheit = c_to_f(0)
