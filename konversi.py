def Celcius(input_nilai):
  '''Celcius'''
  celcius = input_nilai
  fahrenheit =  (9/5) * celcius + 32
  kelvin= celcius + 273.15
  reamur = (4/5) * celcius
  rankine = (celcius + 273.15) * 9/5
  return celcius, fahrenheit, kelvin, reamur, rankine

def Fahrenheit(input_nilai):
  '''Fahrenheit'''
  fahrenheit = input_nilai
  celcius =  (fahrenheit - 32) * 5/9
  kelvin = (fahrenheit + 459.67) * 5/9
  reamur = (4/9) * (fahrenheit - 32)
  rankine = fahrenheit + 459.67
  return fahrenheit,celcius, kelvin, reamur, rankine

def Reamur(input_nilai):
  '''Reamur'''
  reamur = input_nilai
  celcius =  reamur / 0.8
  fahrenheit = (reamur * 2.25) + 32
  kelvin = (celcius) + 273.15
  rankine = (reamur * 2.25) + 491.67
  return reamur, celcius, fahrenheit, kelvin, rankine

def Rankine(input_nilai):
  '''Rankine'''
  rankine = input_nilai
  celcius =  (rankine - 491.67) * (5/9)
  fahrenheit = rankine - 459.67
  kelvin = rankine * (5/9)
  reamur =  (rankine / 1.8 + 273.15) * 0.8
  return rankine, celcius, fahrenheit, kelvin, reamur
  
def Kelvin(input_nilai):
  '''Kelvin'''
  kelvin = input_nilai
  celcius =  kelvin - 273.15
  fahrenheit = (kelvin * (9/5)) - 459.67
  reamur =  4/5 * (kelvin - 273)
  rankine = kelvin * (9/5)
  return kelvin, celcius, fahrenheit, reamur, rankine