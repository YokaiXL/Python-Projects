import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import pandas_ta as ta
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Telegram botu için token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Kripto_Veri fonksiyonunu tanımlayalım.
def Kripto_Veri(sembol):
    mevcut_tarih = datetime.now()
    baslangic_tarihi = mevcut_tarih - timedelta(days=4*365)  # Son 4 yıl
    baslangic_tarihi_str = baslangic_tarihi.strftime('%Y-%m-%d')
    df = yf.download(sembol, start=baslangic_tarihi_str)
    return df

# Supertrend indikatörünü hesaplayan fonksiyonu tanımlayalım
def Supertrend(data, atr_period=10, multiplier=3):
    atr = ta.atr(high=data['High'], low=data['Low'], close=data['Close'], length=atr_period)
    hl2 = (data['High'] + data['Low']) / 2
    supertrend = hl2 - (multiplier * atr)
    return supertrend

# Al sinyali veren kripto para birimlerini kontrol eden fonksiyon
def check_signals(update: Update, context: CallbackContext) -> None:
    semboller = ["BTC-USD", "XRP-USD", "ETH-USD", 
                 "AVAX-USD", "ARK-USD", "ARKM-USD", "ARB-USD","APE-USD",
                 "ALT-USD","AI-USD", "ACH-USD","ALT-USD","APT-USD", "AI-USD","BONK-USD", "BNB-USD","CAKE-USD",
                 "DOGE-USD","ETHFI-USD","FET-USD", "FLOKI-USD","JUP-USD",
                 "PEPE-USD","PYTH-USD","OCEAN-USD", "RNDR-USD", "SOL-USD","SHIB-USD","SHIBA-USD","WIF-USD","ONDO-USD"]
    al_sinyali_verenler = []

    for sembol in semboller:
        data = Kripto_Veri(sembol)
        data['Supertrend'] = Supertrend(data)

        # Son gün için al sinyalini kontrol et
        if data.iloc[-1]['Close'] > data.iloc[-1]['Supertrend']:
            al_sinyali_verenler.append(sembol)

    # Al sinyali veren kripto para birimlerini gönder
    if al_sinyali_verenler:
        sinyal_listesi = "\n".join(al_sinyali_verenler)
        mesaj = f"Al sinyali veren kripto para birimleri:\n{sinyal_listesi}"
    else:
        mesaj = "Hiçbir kripto para biriminden al sinyali gelmedi."

    update.message.reply_text(mesaj)

# Botun ana fonksiyonunu tanımlayalım
async def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # /sinyal komutunu tanımla
    application.add_handler(CommandHandler("sinyal", check_signals))
    
    # Botu başlat
    await application.start()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
