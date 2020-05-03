import requests
import json

url = "https://covid-19-data.p.rapidapi.com/country/all"


headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "219af233afmshaeb5e98710dbbe1p1d4233jsn0eceb506aa8a"
}

response = requests.request("GET", url, headers=headers)
res = response.json()
s = [(res[i]["confirmed"],res[i]["country"]) for i in range(0, len(res)-1)]
result = sorted(s, reverse=True)
print("Showing the details of top Ten Countries affected by Corona Virus")
for i in range(0,10):
    print(f"Number of person affected by Corona Virus in {result[i][1]} is:{result[i][0]}")