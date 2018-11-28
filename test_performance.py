import http.client, random, sys, time
from queue import Queue
from threading import Thread

# 1
# simple : 0.5062289237976074
# load balanced : 0.5068542957305908

# 5
# simple : 1.5106291770935059
# load balanced : 0.9076131343841553

# 10
# simple : 2.763799524307251
# load balanced : 1.5100840091705323

# 15
# simple : 4.023359759648641
# load balanced : 2.1469605445861815

# 20
# simple : 4.60670313835144
# load balanced : 2.763711988925934

# 25
# simple : 6.053423824310303
# load balanced : 3.3995273876190186

# 30
# simple : 6.327429262797038
# load balanced : 4.027852781613668

def doWork(results):
        requests.get()
        
        try:
            connection = http.client.HTTPConnection("132.207.12.86", 8080)
            start = time.time()
            connection.request("GET", "/")
            response = connection.getresponse()
            end = time.time()
            results.put(end - start)
        except:
            connection = http.client.HTTPConnection("132.207.12.86", 8080)
            start = time.time()
            connection.request("GET", "/")
            response = connection.getresponse()
            end = time.time()
            results.put(end - start)

        requests.task_done()

concurrent = 1
requests = Queue(concurrent)
results = Queue(concurrent)

# Initiate concurrent threads
for i in range(concurrent):
    t = Thread(target=doWork, args=[results])
    t.daemon = True
    t.start()

# Send http requests
for url in range(concurrent):
    requests.put("http request")
requests.join()

# Calculate average time
average_time = 0
for result in list(results.queue):
    average_time = average_time + result
average_time = average_time / concurrent

print("Temps d'exécution moyen : " + str(average_time))
