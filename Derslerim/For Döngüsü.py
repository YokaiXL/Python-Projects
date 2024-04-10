
#* Sırasıyla numbers içindeki elemanları yazdıralım.
numbers = [1,2,3,4,5,6,7]
for x in numbers:
    print(x)

#* Numbers içindeki sayıları birer artırıp ekrana yazdıralım.
for x in numbers:
    x+=1
    print(x)
#* Listedeki isimleri döngüye alalım.
names = ["Taha", "Saim", "Yahya"]
for x in names:
    print(f"Benim adım {x}")

#* Verinin her elemanını teker teker yazdıralım.
soyad= "Aslanhan"
for s in soyad:
    print(s)

#* Sıralı elemanları x,y şeklinde ayıralım.
tuple = [(1,2),(3,4),(5,6),(7,8)]
for a,b in tuple:
    print(a)
    print(b)

#* Dictionary içindeki keyleri yazdıralım.
dict = {"isim":"Taha", "soyisim":"Aslanhan", "yaş":19}
for item in dict:
    print(item)

#* Dictionary içindeki verileri yazdıralım.

dict = {"isim":"Taha", "soyisim":"Aslanhan", "yaş":19}
for item in dict.values():
    print(item)

#* Dictionary içindeki itemleri yazdıralım.
dict = {"isim":"Taha", "soyisim":"Aslanhan", "yaş":19}
for item in dict.items():
    print(item)

#* Dictionary içindeki key ve value'ları ayıralım.
dict = {"isim":"Taha", "soyisim":"Aslanhan", "yaş":19}
for key, value in dict.items():
    print(key)
    print(value)

#* break komutunu tanıyalım.
meyveler= ["elma", "armut", "muz", "çilek", "karpuz"]
for meyve in meyveler:
    print(meyve)
    if meyve == "muz":
        break

#* break komutunu print komutundan sonra tanımlayalım.
sebzeler = ["domates", "patlıcan","biber","kabak","patates"]
for sebze in sebzeler:
    if sebze == "biber":
        break
    print(sebze) #Yukarıda eşitliği yazdırdık ancak burada print komutu sona yazıldığı için eşitliği yazdırmadık.

#* continue komutunu tanıyalım.
isimler= ["Taha", "Saim", "Yahya", "Mehmet", "Ali"]
for isim in isimler:
    if isim == "Yahya":
        continue
    print(isim) #Yahya'yı yazdırmadık.

#* range fonksiyonunu tanıyalım.
for x in range(10):
    print(x) #0'dan 9'a kadar sayıları yazdırdık. 10 dahil değil.

for y in range(2,8):
    print(y) #2'den 7'e kadar sayıları yazdırdık. 8 dahil değil.

for z in range(2,19,4):
    print(z) #Sayıları 4 arttırarak 2'den 18'e kadar sayıları yazdırdık. 19 dahil değil.

#* if else yapısını kullanarak döngüyü durduralım.
for a in range(20,42):
    if a == 35: break
    print(a)
else:
    print("Buraya kadardı.")

#* İki ayrı listedeki elemanları ikili şekilde yazalım.
liste1 = [1,2,3]
liste2 = [4,5,6]
for i in liste1:
    for j in liste2:
        print(i,j)

#* Hata aldığımız döngüyü pass komutu ile geçeriz.
for a in [1,2,3,4]:
    pass