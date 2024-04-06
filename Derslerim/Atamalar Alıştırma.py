x, y, z = 2,5,10
numbers = 1,5,7,10,6

#*Kullanıcıdan aldığımız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
sayiKullanici= int(input("İlk sayıyı giriniz: "))
sayiKullanici2= int(input("İkinci sayıyı giriniz: "))
sonuc = sayiKullanici*sayiKullanici2 - (x+y+z)
print(sonuc)

#* y'nin x'e kalansız bölümünü hesaplayınız.
sonuc2 = y//x
print(sonuc2)

#* x,y,z toplamının mod 3'ünü hesaplayınız.
sonuc3 = (x+y+z)%3
print(sonuc3)

#* y'nin x. kuvvetini hesaplayınız.
sonuc4 = y**x
print(sonuc4)