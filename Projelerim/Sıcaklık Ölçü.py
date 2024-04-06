print("Sıcaklık Dönüştürücüye Hoş Geldin!")
from time import sleep
sleep(2)
print("Lütfen Yapmak İstediğin İşlemin Numarasını Gir.")


print("1- Santigrat to Kelvin\n2- Kelvin to Santigrat\n")
islem_no = input()

if islem_no == "1":
    print("Santigrat cinsinden sıcaklığı giriniz.")
    santigrat = int(input())
    kelvin_sonuc = santigrat + 273,15
    print("Kelvin cinsinden sıcaklık değeri: ",kelvin_sonuc)

else:
    print("Kelvin cinsinden sıcaklığı giriniz. ")
    kelvin = int(input())
    santigrat_sonuc = kelvin - 273,15
    print("Santigrat cinsinden sıcaklık değeri:",santigrat_sonuc)
    
