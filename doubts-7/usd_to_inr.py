import requests

money=int(input("enter Dollars:    "))

url="https://currencyapi.net/api/v1/rates?key=AZcoollxIoPSPU9G5GeS6rsOtf9odRYRATKw"

respnse=requests.get(url)
data=respnse.json()

print("$",money,"=","Rs",money*data["rates"]["INR"])


