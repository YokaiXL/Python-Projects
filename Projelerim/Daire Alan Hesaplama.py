print("Alan Hesaplayıcıya Hoş Geldiniz.")
from time import sleep # Modülü ekledik
sleep(2)
print("Lütfen alanını hesaplamak istediğin dairenin yarı çapını giriniz.")
yaricap = float(input())
alan = 3.14 * yaricap*yaricap
print("Alan: " , alan) # Virgüle dikkat et, mal gibi + koyma. Burası C# değil!