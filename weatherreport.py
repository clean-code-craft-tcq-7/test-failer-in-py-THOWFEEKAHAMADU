def report(sensor_reader):
    data = sensor_reader()
    temp_weather = "Sunny Day"

    precipitation = data.get("precipitation", 0)
    wind = data.get("wind_speed_kmph", 0)

    if precipitation <= 0:
        return temp_weather

    if precipitation >= 20 and precipitation < 60:
        return "raining and partly cloudy"
    if wind > 50:
        return "Alert, Stormy with heavy rain"

    return "rainy day"
