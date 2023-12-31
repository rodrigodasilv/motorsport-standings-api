from flask import Flask
import requests
import json
import datetime
from bs4 import BeautifulSoup
from waitress import serve

app = Flask(__name__)

current_year = datetime.date.today().year
def get_data(url, competitors_nr):
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    data = []
    for competitors in soup.find_all("tr", class_="competitor"):
        position = int(competitors.find("td", class_="position").text)
        driver = competitors.find("div", class_="name").text.upper().strip()
        driver_surname = driver.split()[1].strip()
        driver_name = driver.split()[0].strip()
        if hasattr(competitors.find("div", class_="country"), 'text'):
            country = competitors.find("div", class_="country").text.strip()
        else:
            country = None
        points = int(competitors.find("td", class_="points").text[:-3])
        driver_data = {'position': position, 'driver': driver, 'driver_surname': driver_surname,
                       'driver_name': driver_name, 'country': country, 'points': points}
        data.append(driver_data)
        json_data = json.dumps(data, ensure_ascii=False)
        if position == competitors_nr:
            break
    return json_data


@app.route('/wrc/<competitors>')
@app.route('/wrc')
def get_standings_wrc(competitors=10):
    return get_data(
        f'https://www.fia.com/events/world-rally-championship/season-{current_year}/standings',
        int(competitors))


@app.route('/f1/<competitors>')
@app.route('/f1')
def get_standings_f1(competitors=20):
    return get_data(
        f'https://www.fia.com/events/fia-formula-one-world-championship/season-{current_year}/{current_year}-classifications',
        int(competitors))


@app.route('/wec/<competitors>')
@app.route('/wec')
def get_standings_wec(competitors=10):
    return get_data(
        f'https://www.fia.com/events/world-endurance-championship/season-{current_year}/standings',
        int(competitors))


print(f'*** Running on http://localhost:8080/ ***')
serve(app, host="0.0.0.0", port=8080)
