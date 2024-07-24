# REFERENSI: https://www.cnnindonesia.com/edukasi/20231018163336-569-1012927/mengenal-skala-dan-konversi-suhu-dilengkapi-cara-menghitungnya
# Menggunakan Paradigma ✨Procedural✨

import os
from time import sleep
os.system('cls')

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

# Program Akan Berjalan Terus Menerus
def main():
  while True:
    os.system("cls")
    
    # Banner
    print("="*30)
    print("*** Konversi Satuan Suhu🌡️  ***")
    print("="*30)
    
    # Input Nilai
    input_nilai = float(input("Input Nilai       : "))
    print("="*30)
    
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Reamur")
    print("4. Rankine")
    print("5. Kelvin")
    print("="*30)
    # print("0. Keluar Program")
    # print("="*28)
    
    # Input Satuan
    pilih_satuan = int(input("Pilih Satuan      : "))
    print("="*30)

    if pilih_satuan == 1:
      celcius, fahrenheit, kelvin, reamur, rankine = Celcius(input_nilai=input_nilai)
      print(f"Celcius    = {celcius:.2f}°C")
      print(f"Fahrenheit = {fahrenheit:.2f}°F")
      print(f"kelvin     = {kelvin:.2f}K")
      print(f"Reamur     = {reamur:.2f}°R")
      print(f"Rankine    = {rankine:.2f}°Ra") 
      print("")
      sleep(5)
      
    elif pilih_satuan == 2:
      fahrenheit, celcius, kelvin, reamur, rankine = Fahrenheit(input_nilai=input_nilai)
      print(f"Fahrenheit = {fahrenheit:.2f}°F")
      print(f"Celcius    = {celcius:.2f}°C")
      print(f"kelvin     = {kelvin:.2f}K")
      print(f"Reamur     = {reamur:.2f}°R")
      print(f"Rankine    = {rankine:.2f}°Ra")
      print("")
      sleep(5)
      
    elif pilih_satuan == 3:
      reamur, celcius, fahrenheit, kelvin, rankine = Reamur(input_nilai=input_nilai)
      print(f"Fahrenheit = {fahrenheit:.2f}°F")
      print(f"Celcius    = {celcius:.2f}°C")
      print(f"kelvin     = {kelvin:.2f}K")
      print(f"Reamur     = {reamur:.2f}°R")
      print(f"Rankine    = {rankine:.2f}°Ra")
      print("")
      sleep(5)
      
    elif pilih_satuan == 4:
      rankine, celcius, fahrenheit, kelvin, reamur  = Rankine(input_nilai=input_nilai)
      print(f"Rankine    = {rankine:.2f}°Ra")
      print(f"Celcius    = {celcius:.2f}°C")
      print(f"Fahrenheit = {fahrenheit:.2f}°F")
      print(f"kelvin     = {kelvin:.2f}K")
      print(f"Reamur     = {reamur:.2f}°R")
      print("")
      sleep(5)
      
    elif pilih_satuan == 5:
      kelvin, celcius, fahrenheit, reamur, rankine  = Kelvin(input_nilai=input_nilai)
      print(f"kelvin     = {kelvin:.2f}K")
      print(f"Celcius    = {celcius:.2f}°C")
      print(f"Fahrenheit = {fahrenheit:.2f}°F")
      print(f"Reamur     = {reamur:.2f}°R")
      print(f"Rankine    = {rankine:.2f}°Ra")
      print("")
      sleep(5)
      
    # elif pilih_satuan == 0:
    #   break
    
    else:
      print("")
      print("Pilihan yang Anda masukkan salah!, Silahkan ulangi kembali 🔁")
      sleep(5)
      continue
    
if __name__ == "__main__":
  main()