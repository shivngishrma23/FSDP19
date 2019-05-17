import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content
jsondata= response.json()

print("latitude and longitude ",jsondata["coord"])
print("weather conditions",jsondata["main"])
print("wind speed",jsondata["wind"]["speed"])
print("sunset",jsondata["sys"]["sunset"])
print("sunrise",jsondata["sys"]["sunrise"])