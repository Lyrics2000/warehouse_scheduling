import requests

url = "https://graph.facebook.com/v13.0/122691670352624?access_token=EAAn35pZA9IZCsBALcGURQzXHNZBZA7stQ5KZAquHvvBcb0D2AIZBhtnZAPBA0CJtGYyHkvquK86BVjVZBaJr5SxJMIxBFBVIkA9OUZBH4P0cBGICkOeZAx93wpDWRVM9HX68aVHLnVyORDp0mjtr4H2uqKdoBY6wVEeZBmZA2sZAjnRAcRyJJcqHmH4ye5T31BaKOTZBdyNnmSQbfytAZDZD"

payload={}
headers = {
  'Cookie': 'c_user=100078353754869; fr=0fVIwS1cducueX3vm.AWXjYsN3nTztZtkdDfGNaFem-r0.BiPJ_U.xF.AAA.0.0.BiPJ_U.AWXNUfB0zsg; xs=7%3ADHq-9iDwJdoLMw%3A2%3A1648132481%3A-1%3A10713%3A%3AAcVBa1kN1FhqoZ0CKPmzUJ0KAkqQ5PreRW5fJ012xQ'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
