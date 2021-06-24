from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, redirect
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import requests
import lxml
app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["GET", "POST"])
def main():
    weather_dict = {'desc': '', 'degree': 0, 'location': '', 'wind': '', 'tmro': '', 'day_after': ''}
    return render_template("main.html", content=weather_dict)


@app.route("/getweather", methods=["GET", "POST"])
def getweather():
    try:
        if request.method == "POST":
            weather_dict = {}
            weather_dict['location'] = request.form["weathertext"]
            response = requests.get('https://goweather.herokuapp.com/weather/'+request.form["weathertext"]+'').json()
            weather_dict['desc'] = response['description']
            weather_dict['degree'] = int(response['temperature'].strip('+ °C'))
            weather_dict['wind'] = response['wind']
            weather_dict['tmro'] = response['forecast'][0]['temperature'].strip('+ °C')
            weather_dict['day_after'] = response['forecast'][1]['temperature'].strip('+ °C')
            print(weather_dict)
            return render_template("main.html", content=weather_dict)
            # res = requests.get('https://www.google.com/search?q=weather+'+location+'').content
            # response = BeautifulSoup(res, "lxml")
            # data = response.find("div", class_='VQF4g')
            # print(data)
            # degree = response.find("span", class_='wob_t TVtOme').text
            # degree = int(degree)
            # desc = response.find("div", class_='wob_dcp').text
            # location = response.find("div", attrs={'id': 'wob_loc'}).text
            # print(location)
            # humidity = response.find("span", class_='wob_hm').text
            # wind = response.find("span", class_='wob_t').text
            # time = response.find("div", class_='wob_dts').text
            # weather_dict = {'desc': desc, 'degree': degree, 'location': location, 'message': "hello", 'humidity': humidity, 'wind': wind, 'time': time}
            # return render_template("main.html", content=weather_dict)
            #
            # response = requests.get('https://weather.codes/search/?q=' + location + '').text
            # countrycode = BeautifulSoup(response, "lxml")
            # ans = countrycode.find("div", class_='country__codes')
            # cc = ans.find("span").text
            # print(cc)
            # weatherresp = requests.get('https://weather.com/en-IN/weather/today/l/' + cc + '').text
            # rep = BeautifulSoup(weatherresp, "lxml")
            # desc = rep.find("div", class_='CurrentConditions--phraseValue--mZC_p').text
            # degree = rep.find("span", class_='CurrentConditions--tempValue--MHmYY').text
            # deg = int(degree.strip('°'))
            # rr = rep.find("div", class_='CurrentConditions--primary--2DOqs').text
            # time = rep.find("div", class_='CurrentConditions--timestamp--1ybTk').text
            # chance = rep.find("div", class_='CurrentConditions--precipValue--2aJSf').text
            # aqi = rep.find("div", class_='AirQuality--col--3I-4C').text
            # cards = rep.find_all("div", class_='ListItem--listItem--25ojW WeatherDetailsListItem--WeatherDetailsListItem--1CnRC')
            # w = cards[1]
            # wind = w.find("span", class_='Wind--windWrapper--3Ly7c undefined').text
            # wind = wind.lstrip("Wind Direction")
            # h = cards[2]
            # humidity = h.find("div", class_='WeatherDetailsListItem--wxData--kK35q').text
            # print(humidity)
            # print(wind)
            # print(aqi)
            # # print('It is currently (in celsius) {0} in {1} {2} with a {3}'.format(rr, location, time, chance))
            # weather = f'''It is currently (in celsius) {rr} in {location} {time} with a {chance}'''
            # weather_dict = {'desc': desc, 'degree': degree, 'location': location, 'message': "hello", 'deg': deg, 'humidity': humidity, 'wind': wind, 'aqi': aqi}
            # return render_template("main.html", content=weather_dict)
            # # return redirect(url_for('main'), content=weather)
    except AttributeError as e:
        print(e)
        weather_dict = {'desc': 'Please check location string again', 'degree': 0, 'location': 'You may want to consider typos in your search string', 'wind': '', 'tmro': '', 'day_after': ''}
        return render_template("main.html", content=weather_dict)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)
