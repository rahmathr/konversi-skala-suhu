# Sumber: https://www.cnnindonesia.com/edukasi/20231018163336-569-1012927/mengenal-skala-dan-konversi-suhu-dilengkapi-cara-menghitungnya

import os
from time import sleep
os.system('cls')

def celcius_to_fahrenheit():
  '''Celsius to Fahrenheit conversion function'''
  print("\n=== KONVERSI Celcius ke Fahrenheit ===")
  celsius = float(input("Masukkan temperature Celsius: "))
  fahrenheit = (celsius * 9/5) + 32
  print(f"{celsius}°C = {fahrenheit}°F")

def celcius_to_reamur():
  '''Celsius to reamur conversion function'''
  print("\n=== KONVERSI Celcius ke Reamur ===")
  celsius = float(input("Masukkan temperature Celsius: "))
  reamur = 4/5 * celsius
  print(f"{celsius}°C = {reamur}°R")

def celcius_to_kelvin():
  '''Celsius to kelvin conversion function'''
  print("\n=== KONVERSI Celcius ke Kelvin ===")
  celsius = float(input("Masukkan temperature Celsius: "))
  kelvin = celsius + 273.15
  print(f"{celsius}°C = {kelvin}K")

def reamur_to_fahrenheit():
  '''Celsius to reamur conversion'''
  print("\n=== KONVERSI Reamur ke Fahrenheit ===")
  reamur = float(input("Masukkan temperature Reamur: "))
  celsius = (5/4 * reamur) - 273.15
  fahrenheit = (celsius * 9/5) + 32
  print(f"{reamur}°R = {fahrenheit}°F")

while True:
  os.system("cls")
  print("=== KONVERSI SKALA SUHU ===")
  print("===========================")
  print("1. Celcius ke Fahrenheit")
  print("2. Celcius ke Reamur")
  print("3. Rumus Celcius ke Kelvin")
  print("4. Reamur ke Fahrenheit")
  print("===========================")
  print("0. Keluar Program")
  print("===========================")
  pilihan = int(input("Silahkan Pilih No. : "))

  if pilihan == 1:
    celcius_to_fahrenheit()
    
  elif pilihan == 2:
    celcius_to_reamur()
    
  elif pilihan == 3:
    celcius_to_kelvin()
    
  elif pilihan == 4:
    reamur_to_fahrenheit()
    
  elif pilihan == 0:
    break
  
  else:
    print("")
    print("Pilihan yang Anda masukkan salah!")
    sleep(5)
    continue
