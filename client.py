import http.client

connection = http.client.HTTPConnection("132.207.12.228", 8080)
connection.request("GET", "/")
response = connection.getresponse()
print(response.read())