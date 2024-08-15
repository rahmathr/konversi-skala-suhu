import os
import temperature_scale_conversion as calculator_result
os.system('cls')

if __name__ == "__main__":
  while True:
    os.system("cls")
    calculator_result.header()

    input_nilai = float(input("Input Nilai       : "))
    print("="*30)
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Reamur")
    print("4. Rankine")
    print("5. Kelvin")
    print("="*30)
    pilih_satuan = int(input("Pilih Satuan      : "))
    print("="*30)

    if pilih_satuan == 1:
      calculator_result.celcius(input_nilai=input_nilai)

    elif pilih_satuan == 2:
      calculator_result.fahrenheit(input_nilai=input_nilai)

    elif pilih_satuan == 3:
      calculator_result.reamur(input_nilai=input_nilai)

    elif pilih_satuan == 4:
      calculator_result.rankine(input_nilai=input_nilai)

    elif pilih_satuan == 5:
      calculator_result.kelvin(input_nilai=input_nilai)