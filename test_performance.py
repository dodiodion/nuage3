import http.client, random, sys, time
from queue import Queue
from threading import Thread

def doWork(results):
    while True:
        requests.get()
        #connection = http.client.HTTPConnection("132.207.12.228", 8080)
        #start = time.time()
        #connection.request("GET", "/")
        #response = connection.getresponse()
        #end = time.time()
        results.put(random.random())
        requests.task_done()

concurrent = 30
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
