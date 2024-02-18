print ("hello")
import psycopg2
import requests
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pycountry




def get_weather(city, api_key):
    # Hava durumu bilgisi almak için API URL'si
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    # Hava durumu API'sine istek gönder
    response = requests.get(api_url)
    data = response.json()
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    weather_date= datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M')
    country_code = data['sys']['country'] 
           

    # Hava durumu bilgilerini yazdır
    print(" Weather Report:")
    print(f"Country Code        :{country_code}")
    print(f"Weather Date        :{weather_date}")
    print(f"Current_Date        :{current_date_time}")
    print(f"Ctiy Name          : {data['name']}")
    print(f"Weather Description: {data['weather'][0]['description']}")
    print(f"Temparature        : {data['main']['temp']} °C")
    print(f"Humidity           : {data['main']['humidity']}%")

# Belirli bir saat ve dakikada sorgu yapmak için bir fonksiyon
def query_at_specific_time(city, api_key):
    get_weather(city, api_key)

query_at_specific_time('Istanbul', 'b9367b3ffdf4bf82d6533268902b088e')
           

# Istanbul'daki hava durumunu sorgula

#query_at_specific_time('Istanbul', 'b9367b3ffdf4bf82d6533268902b088e')

def send_email(subject, body, to_email):
    # Gönderen e-posta bilgileri
    from_email = "sbncan377@gmail.com"
    email_password = "scqr dwix fanz xvhx"

    # E-posta oluşturma
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # E-posta gövdesi
    msg.attach(MIMEText(body, 'plain'))

    # SMTP sunucusuna bağlanma
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, email_password)

        # E-posta gönderme
        server.sendmail(from_email, to_email, msg.as_string())

# Örnek kullanım
subject = "Test E-posta"
#body = (f"Şehir: {weather_data['name']} saat : {arget_hour}:{target_minute} Sıcaklık: {weather_data['main']['temp']} Kelvin" )   
body ="Rapor alindi"
to_email = "serhatglck41@gmail.com"

send_email(subject, body, to_email) 