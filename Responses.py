# encoding:utf-8
from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("sa", "meraba", "selam", "merhaba", "Selamünaleyküm"):
        return "Merhaba, Nasıl gidiyor?"

    if user_message in ("iyi", "fena değil", "idare eder", "güzel", "ii"):
        return "Bunu duyduğuma sevindim 😊" + "New"

    if user_message in ("kötü", "sorma ya", "off", "Kötüyüm", "Kötü hissediyorum"):
        return "Noldu neyin var :("

    if user_message in ("sen kimsin", "kimsin", "nesin", "kendini tanıt"):
        return "Ben bir botum"

    if user_message in ("hız ve hareket"):
        return "Hız V harfi ile gösterilir ve SI'da birimi m/s dir."

    if user_message in ("pisagor", "pisagor teoremi", "pisagor üçgeni", "pisagor formülü"):
        return "Uzun bir açıklama istersen bir dik üçgen düşündüğümüzde, dik açının karşısındaki kenarın uzunluğu diğer iki kenarın karesinin toplamına eşittir"


    if user_message in ("zaman", "saat", "saat kaç?", "saati söyle"):
        now = datetime.now()
        date_time = now.strftime("%%H:%M:%S")


    if user_message in ("tarih"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Dediğinizi anlayamadım"