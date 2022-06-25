# IMPORTING LIBRARIES
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# CONSTANTS
# WEATHER
OWM_API_KEY = os.environ.get("OWM_API_KEY")
MY_LATITUDE = os.environ.get("LATITUDE")
MY_LONGITUDE = os.environ.get("LONGITUDE")
OWM_API_ENDPOINT = os.environ.get("OWM_API_ENPOINT")
CLEAR_SKY_CODE = 800
NUM_HOURS = 12

# TWILIO
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM_MOBILE_NUMBER = os.environ.get("FROM_NUMBER")
TO_MOBILE_NUMBER = os.environ.get("TO_NUMBER")


parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily,alerts",
}


weather_response = requests.get(url=OWM_API_ENDPOINT, params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
subject = ""

will_rain = False

for i in range(NUM_HOURS):
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_code < CLEAR_SKY_CODE:
        hours = "hour" if (i == 0) else "hours"
        subject = f"It will rain {i + 1} {hours} from now. ☂️"
        will_rain = True
        break

proxy_client = TwilioHttpClient(
    proxy={"http": os.environ["http_proxy"], "https": os.environ["https_proxy"]}
)


if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body=subject,
        from_=FROM_MOBILE_NUMBER,
        to=TO_MOBILE_NUMBER,
    )

print(message.status)
