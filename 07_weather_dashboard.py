import requests
def get_weather():
    while True:
        city = input("Enter the city you want to search or q to quit:")
        if city == "q":
            break

        geo_url =  f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_req = requests.get(geo_url)
        geo_data = geo_req.json()
        if "results" not in geo_data:
            print("City not found!!")
            continue
        else:
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        weather_data = response.json()
        current = weather_data["current_weather"]
        temp = current["temperature"]
        wind_spd = current["windspeed"]
        print(f"THe current temperature is {temp}C and the current windspeed is {wind_spd}km/h")
get_weather()