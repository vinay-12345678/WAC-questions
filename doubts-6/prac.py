import requests

url="https://currencyapi.net/api/v1/rates?key=AZcoollxIoPSPU9G5GeS6rsOtf9odRYRATKw"

respnse=requests.get(url)
data=respnse.json()

for i in data.keys():
    if(i=="rates"):
        for x in data[i]:
            if(x=="INR"):
                print(x,data[i][x])