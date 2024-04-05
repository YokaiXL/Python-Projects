#Cenk ismini listenin sonuna ekleyelim.
isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli"]
isimler.append("Cenk")

#Sena ismini listenin başına ekleyelim.
isimler.insert(0, "Sena")

#Ali ismini listeden silelim.
isimler.remove("Ali") # pop(4) ile de silebilirdim.

#Fatma isminin index'ini bulalım.
print(isimler.index("Fatma"))

#Ayşe isminin listede olup olmadığını test edelim.
test = isimler.index("Ayşe")
print(test)

#Liste elemanlarını ters çevirelim.
isimler.reverse()
print(isimler)

#Listedeki elemanları alfabetik olarak sıralayalım.
isimler.sort()

print(isimler)

#String dizisini listeye çevirelim.
str = "Kawasaki", "KTM", "Yamaha" , "Honda"
marka =list(str) 
print(marka)


#Sayılar listesinin en büyük ve en küçük değerini bulalım
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(sayilar))
print(min(sayilar))

#Kullanıcıdan aldığımız veriyi Sayılar listemize ekleyelim.
sayi = int(input("Bir sayı giriniz: "))
sayilar.append(sayi)
print(sayilar)

