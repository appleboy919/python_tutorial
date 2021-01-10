import urllib.request
import json


def printResults(data):
    # use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    # for each event, print the place where it occured
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("---------------")

    # print the events that only have a magnitude greater than 3
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 3.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
        print("---------------")

    # print only the evets where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]
                      ["place"], "reported " + str(feltReports) + " times")


def main():
    # define a variable to hold the source URL
    # in this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"

    # open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Receied error, cannot parse results")


if __name__ == "__main__":
    main()

### Note ###
# 1: JSON: Javascript object notation
# 2: %2.1f --> 2 significant digits + 1 decimal digit
# 3: for more information about JSON handling, https://docs.python.org/3.8/library/json.html
