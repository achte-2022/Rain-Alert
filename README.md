# Rain-Alert

### [twitter](https://twitter.com/achte_te)

## Description
A program that send text messages using Twilio API, if it rains within the next 12 hours. Weather data is obtained using OpenWeatherMap API. The code is hosted on [pythonanywhere](https://www.pythonanywhere.com/).  

## Requirements

[Python](https://www.python.org/)

```sh
$ python3 --version
Python 3.9.12
```

[os](https://docs.python.org/3/library/os.html)

[requests](https://pypi.org/project/requests/)

[OpenWeatherMap API](https://openweathermap.org/api)

[twilio](https://www.twilio.com/)

## Install

```sh
$ git clone git@github.com:achte-2022/Rain-Alert.git
```

## Run 

### Environment Variables are DUMMY values

```sh
$ cd Rain-Alert
# SETTING ENVIRONMENT VARIABLES
$ export OWM_API_KEY=6sd2f85sdf2sdf;
$ export LATITUDE=11.004107;
$ export LONGITUDE=-74.806984;
$ export OWM_API_ENPOINT=https://api.openweathermap.org/data/2.5/onecall;
$ export AUTH_TOKEN=1sd5f2c5s5fs;
$ export AUTH_SID=s2f5s6f5c2skskc;
$ export TO_NUMBER=+11111111111;
$ export FROM_NUMBER=+100000000;
#RUNNING MAIN PROGRAM
$ python3 main.py
```

## Text Message
![](images/text.jpg)