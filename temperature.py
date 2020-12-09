def main():
    """check the temperature in Bangkok, Thailand"""
    import requests
    api_address='http://api.openweathermap.org/data/2.5/weather?q=Bangkok&appid=9486b253fad80b593ccee78727b6e327&units=metric'
    json_data = requests.get(api_address).json()
    temperature = json_data['main']['temp']
    print("%.2f Celcius" % temperature)
main()
