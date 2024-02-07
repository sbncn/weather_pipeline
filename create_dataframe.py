from datetime import datetime
import pandas as pd





def create_dataframe_from_weather(weather_data, city):
    weather_date = datetime.utcfromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M')
    country_code = weather_data['sys']['country']
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    df = pd.DataFrame({
        'country_codes': [country_code],
        'city': [city],
        'temperature': [weather_data['main']['temp']],
        'humidity': [weather_data['main']['humidity']],
        'weather_description': [weather_data['weather'][0]['description']],
        'weather_date': [weather_date],
        'query_date': [current_date_time]
    })
    return df

    #print(weather_data["dt"])