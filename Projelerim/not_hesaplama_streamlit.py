import streamlit as st

def calculate_grade(vize, final, vize_yuzde, final_yuzde, final_min):
    total = int((vize * vize_yuzde / 100) + (final * final_yuzde / 100))
    if total >= 90:
        return "AA Not ile geçtiniz."
    elif 80 <= total < 90:
        return "BA Not ile geçtiniz."
    elif 70 <= total < 80:
        return "BB Not ile geçtiniz."
    elif 60 <= total < 70:
        return "CB Not ile geçtiniz."
    elif 50 <= total < 60:
        return "CC Not ile kaldınız."
    elif 40 <= total < 50:
        return "DC Not ile kaldınız."
    elif 30 <= total < 40:
        return "DD Not kaldınız."
    elif 20 <= total < 30:
        return "FD Not ile kaldınız."
    else:
        return "FF Not ile sınıfta kaldınız."

def main():
    st.title("Not Hesaplayıcı Programa Hoş Geldiniz.")
    st.write("Programımız tek dönemlik dersler için geçerlidir. İki vizesi olan dersler için kullanılamaz.")

    vize = st.number_input("Lütfen İlk Vize Notunuzu Giriniz:", min_value=0, max_value=100, step=1)
    final = st.number_input("Lütfen Final Notunuzu Giriniz:", min_value=0, max_value=100, step=1)

    vize_yuzde = st.number_input("Vize notunuzun ortalamayı yüzde kaç etkilediğini giriniz:", min_value=0, max_value=100, step=1)
    final_yuzde = st.number_input("Final notunuzun ortalamayı yüzde kaç etkilediğini giriniz:", min_value=0, max_value=100, step=1)

    final_min = st.number_input("Lütfen minimum almanız gereken final notunu giriniz:", min_value=0, max_value=100, step=1)

    if st.button("Hesapla"):
        result = calculate_grade(vize, final, vize_yuzde, final_yuzde, final_min)
        st.write("Sonuç:", result)

if __name__ == "__main__":
    main()
