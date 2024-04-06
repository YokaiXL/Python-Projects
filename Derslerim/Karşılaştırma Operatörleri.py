#Basit olarak iki veriyi karşılaştıralım.
a = 5
b = 10
sonuc = a==b
print(sonuc) #* False çıktısını verdi çünkü 5 ile 10 eşit değil.

#Kullanıcıdan alınan şifrenin eşleşip eşleşmediğini bulalım. (1)
password = "siberkoza"
passwd = input("Şifreyi giriniz: ")

if password == passwd:
    print("Şifre eşleşmiştir.")
else:
    print("Şifre eşleşmedi.")

#Kullanıcıdan alınan şifrenin eşleşip eşleşmediğini bulalım. (2)

password = "siberkoza"
passwd = input("Şifreyi giriniz: ")
result = password == passwd
print(result)

