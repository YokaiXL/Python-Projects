#Motor markaları ile fiyatlarını eşleştirelim.
fiyat = {
    "KTM" : {
        "125duke" : 252000,
        "390duke" : 346900,
        "990duke" : 702000,
    },

    "YAMAHA" : {
        "MT-25" : 260300,
        "R25" : 272600,
        "R7" : 453300,
    },
    "HONDA" : {
        "CBR650R" : 521000,
        "CBR10000RR" : 1543000,
 
    }   
}
print(fiyat[input("Markayı giriniz: ")][input("Modeli giriniz: ")])

#!Virgüllerin yerlerine dikkat et!