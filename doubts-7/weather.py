import requests

place=input("enter city:    ")

url="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid=86b010f6db27510ca1e7f23ac96a3f0b"
response=requests.get(url)
data=response.json()
print()
temp=data["main"]["temp"]
print(data["name"],temp-273.15)