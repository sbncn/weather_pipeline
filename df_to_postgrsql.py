from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def write_dataframe_to_postgres(df):

    db_config = getenv("db_config")

    engine = create_engine(db_config)

    df.to_sql('weather_city', engine, if_exists='append', index=False)

    engine.dispose()





