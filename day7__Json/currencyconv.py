import requests
url1 ="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR&compact=y"
url3=" &apiKey=c4744554dd1a1d4bdddc"
url = url1+url2+url3
response = requests.get(url)
response.content

data= response.json()
value= data["results"]["USD_INR"]["val"]
amount = int(input("enter amount you want to convert"))
INR = amount*value
print(INR)
