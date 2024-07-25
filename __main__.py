# REFERENSI: https://www.cnnindonesia.com/edukasi/20231018163336-569-1012927/mengenal-skala-dan-konversi-suhu-dilengkapi-cara-menghitungnya
# Menggunakan Paradigma ✨Procedural✨

import os
from time import sleep
from konversi import Celcius,Fahrenheit,Kelvin,Reamur,Rankine

os.system('cls')

# Main Program
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