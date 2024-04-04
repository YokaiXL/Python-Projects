
print("İsminizi Giriniz: ")
isim = input()
from time import sleep
sleep(1)
print("Yaşınızı Giriniz: ") 
yas = input()
metin = "Merhaba! Benim adım {}, ben {} yaşımdayım.".format(isim, yas)


print("İsminizi Giriniz: ")
isim = input()
from time import sleep
sleep(1)
print("Yaşınızı Giriniz: ") 
yas = input()
metin = "Merhaba! Benim adım {i}, ben {y} yaşımdayım.".format(i = isim, y = yas)
print(metin)


print("İsminizi Giriniz: ")
isim = input()
from time import sleep
sleep(1)
print("Yaşınızı Giriniz: ") 
yas = input()
metin = "Merhaba! Benim adım {0}, ben {1} yaşımdayım.".format(i = isim, y = yas)
print(metin)


print("İsminizi Giriniz: ")
isim = input()
from time import sleep
sleep(2)
print("Yaşınızı Giriniz: ") 
yas = input()
metin = (f"Merhaba! Benim adım {isim}, ben {yas} yaşımdayım.")
print(metin)


sonuc = 10/3
print("Sonucunuz {s:1.7}".format(s=sonuc))