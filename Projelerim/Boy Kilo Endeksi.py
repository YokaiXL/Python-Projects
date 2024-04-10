print("Boy-Kilo Endeksi Hesaplama Programına Hoş Geldiniz.")

boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
kilo = float(input("Lütfen kilonuzu kilogram cinsinden giriniz: "))

endeks = kilo / (boy * boy)

if endeks < 18.5:
    print("Ortalamanız {:.2f} düşük kilolusunuz.".format(endeks))
elif 18.5 <= endeks < 25:
    print("Ortalamanız {:.2f} normal kilolusunuz.".format(endeks))
elif 25 <= endeks < 30:
    print("Ortalamanız {:.2f} fazla kilolusunuz.".format(endeks))
elif endeks >= 30:
    print("Ortalamanız {:.2f} obezsiniz.".format(endeks))
else:
    print("Lütfen geçerli bir değer giriniz.")
