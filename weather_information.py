from datetime import datetime
from create_dataframe import create_dataframe_from_weather
from df_to_postgrsql import write_dataframe_to_postgres
from send_mail import send_email
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()

def weather_info():

    api_key = getenv("api_key")
    city = getenv("city")
    base_url = getenv("base_url")

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        country_code = data['sys']['country']
        weather_date = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M')
        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        if response.status_code == 200:
            df = create_dataframe_from_weather(data, city)
            write_dataframe_to_postgres(df)

            send_email(subject=f"statuscode: {response.status_code}", body="operation completed successfully")


            print(f"City Name           :{city}")
            print(f"Country Code        :{country_code}")
            print(f"Weather Date        :{weather_date}")
            print(f"Temperature         :{data['main']['temp']}°C")
            print(f"Humidity            :{data['main']['humidity']}%")
            print(f"Weather Description :{data['weather'][0]['description']}")
            print(f"Current_Date        :{current_date_time}")
        else:
            print(f"Weather information could not be retrieved. Error code: {response.status_code}")
    except Exception as e:
        send_email(subject=f"statuscode: {response.status_code}", body=f"operation could not be completed. Error:{e}")
        print(f"Error: {e}")