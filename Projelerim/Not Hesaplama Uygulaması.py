print("Not Hesaplayıcı Programa Hoş Geldiniz.")
print("Programımız tek dönemlik dersler için geçerlidir. İki vizesi olan dersler için kullanılamaz.")
#Çok fazla print komutu ile kodu kalabalıklaştırdığımın farkındayım. \n ile önüne geçilebilir ama amacım elimin alışmasıdır bu noktada.
print("Lütfen İlk Vize Notunuzu Giriniz: ")
vize= int(input())

print("Lütfen Final Notunuzu Giriniz: ")
final= int(input())

#Yüzdelik dilimler üniversiteye göre değişebiliyor. Programın sağlıklı sonuçlar verebilmesi açısından bu yüzdelikleri kullanıcıdan almayı uygun gördüm.
print("Öncelikle vize notunuzun ortalamayı yüzde kaç etkilediğini, daha sonra final notunuzun ortalamayı yüzde kaç etkilediğini giriniz.")
vize_yuzde= int(input())
final_yuzde= int(input())

print("Lütfen minimum almanız gereken final notunu giriniz:  ")
final_min = int(input())

#İlk başta total değişkenini not diye yazmıştım kod hata verdi. Program not kelimesini bildiğimiz ters fonksiyon olarak  algılamış :DDD
total = int((vize*vize_yuzde) + (final*final_yuzde))

#if-else kod bloğunda 5 satır yazdıktan sonra Co-Pilot diğer elif blokları tamamladı.
if final >=final_min:
    if(total>=90):
        print("AA Not ile geçtiniz.") 
    elif(total>=80 and total<90):
        print("BA Not ile geçtiniz.")
    elif(total>=70 and total<80):
        print("BB Not ile geçtiniz.")
    elif(total>=60 and total<70):
        print("CB Not ile geçtiniz.")
    elif(total>=50 and total<60):
        print("CC Not ile geçtiniz.")
    elif(total>=40 and total<50):
        print("DC Not ile geçtiniz.")
    elif(total>=30 and total<40):
        print("DD Not ile geçtiniz.")
    elif(total>=20 and total<30):
        print("FD Not ile geçtiniz.")
else:
        print("FF Not ile sınıfta kaldınız.")   