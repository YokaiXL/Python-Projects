import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import pandas_ta as ta

# Kripto_Veri fonksiyonunu tanımlayalım.
def Kripto_Veri(sembol):
    mevcut_tarih = datetime.now()
    baslangic_tarihi = mevcut_tarih - timedelta(days=4*365)  # Son 4 yıl
    baslangic_tarihi_str = baslangic_tarihi.strftime('%Y-%m-%d')
    df = yf.download(sembol, start=baslangic_tarihi_str)
    return df

# Supertrend indikatörünü hesaplayan fonksiyonu tanımlayalım
def Supertrend(data, atr_period=10, multiplier=3):
    high_low = (data['High'] + data['Low']) / 2
    atr = ta.atr(data['High'], data['Low'], data['Close'], length=atr_period)
    supertrend = high_low + (multiplier * atr)
    return supertrend

semboller = ["BTC-USD", "XRP-USD", "ETH-USD", 
             "AVAX-USD", "ARK-USD", "ARKM-USD", "ARB-USD","APE-USD",
             "ALT-USD","AI-USD", "ACH-USD","ALT-USD","APT-USD", "AI-USD","BONK-USD", "BNB-USD","CAKE-USD",
             "DOGE-USD","ETHFI-USD","FET-USD", "FLOKI-USD","JUP-USD",
             "PEPE-USD","PYTH-USD","OCEAN-USD", "RNDR-USD", "SOL-USD","SHIB-USD","SHIBA-USD","WIF-USD","ONDO-USD"]
al_sinyali_verenler = []

for sembol in semboller:
    data = Kripto_Veri(sembol)
    data['Supertrend'] = Supertrend(data)

    # Son gün için al sinyalini kontrol et (Fiyat Supertrend değerinin üzerindeyse al sinyali)
    if data.iloc[-1]['Close'] > data.iloc[-1]['Supertrend']:
        al_sinyali_verenler.append(sembol)

# Al sinyali veren kripto para birimlerini yazdırın
if al_sinyali_verenler:
    print("Al sinyali veren kripto para birimleri:")
    for sembol in al_sinyali_verenler:
        print(sembol)
else:
    print("Hiçbir kripto para biriminden al sinyali gelmedi.")