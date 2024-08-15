from time import sleep

def celcius(input_nilai:int):
  celcius = input_nilai
  print(f"Celcius    = {celcius:.2f}°C")
  fahrenheit =  (9/5) * celcius + 32
  print(f"Fahrenheit = {fahrenheit:.2f}°F")
  kelvin= celcius + 273.15
  print(f"kelvin     = {kelvin:.2f}K")
  reamur = (4/5) * celcius
  print(f"Reamur     = {reamur:.2f}°R")
  rankine = (celcius + 273.15) * 9/5
  print(f"Rankine    = {rankine:.2f}°Ra")
  sleep(7)

def fahrenheit(input_nilai:int):
  fahrenheit = input_nilai
  print(f"Fahrenheit = {fahrenheit:.2f}°F")
  celcius =  (fahrenheit - 32) * 5/9
  print(f"Celcius    = {celcius:.2f}°C")
  kelvin = (fahrenheit + 459.67) * 5/9
  print(f"kelvin     = {kelvin:.2f}K")
  reamur = (4/9) * (fahrenheit - 32)
  print(f"Reamur     = {reamur:.2f}°R")
  rankine = fahrenheit + 459.67
  print(f"Rankine    = {rankine:.2f}°Ra")
  sleep(7)

def kelvin(input_nilai:int):
  kelvin = input_nilai
  print(f"kelvin     = {kelvin:.2f}K")
  celcius =  kelvin - 273.15
  print(f"Celcius    = {celcius:.2f}°C")
  fahrenheit = (kelvin * (9/5)) - 459.67
  print(f"Fahrenheit = {fahrenheit:.2f}°F")
  reamur =  4/5 * (kelvin - 273)
  print(f"Reamur     = {reamur:.2f}°R")
  rankine = kelvin * (9/5)
  print(f"Rankine    = {rankine:.2f}°Ra")
  sleep(7)

def reamur(input_nilai:int):
  reamur = input_nilai
  print(f"Reamur     = {reamur:.2f}°R")
  celcius =  reamur / 0.8
  print(f"Celcius    = {celcius:.2f}°C")
  fahrenheit = (reamur * 2.25) + 32
  print(f"Fahrenheit = {fahrenheit:.2f}°F")
  kelvin = (celcius) + 273.15
  print(f"kelvin     = {kelvin:.2f}K")
  rankine = (reamur * 2.25) + 491.67
  print(f"Rankine    = {rankine:.2f}°Ra")
  sleep(7)

def rankine(input_nilai:int):
  rankine = input_nilai
  print(f"Rankine    = {rankine:.2f}°Ra")
  celcius =  (rankine - 491.67) * (5/9)
  print(f"Celcius    = {celcius:.2f}°C")
  fahrenheit = rankine - 459.67
  print(f"Fahrenheit = {fahrenheit:.2f}°F")
  kelvin = rankine * (5/9)
  print(f"kelvin     = {kelvin:.2f}K")
  reamur =  (rankine / 1.8 + 273.15) * 0.8
  print(f"Reamur     = {reamur:.2f}°R")
  sleep(7)