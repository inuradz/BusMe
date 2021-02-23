from flask import Flask, request, Response
import json
from zipfile import ZipFile
import csv
from time import localtime, strftime, strptime
app = Flask(__name__)

def get_bus_number():
    pass

def get_stop_times():
    pass



@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        req_data = request.get_json()
        #print(json.dumps(req_data, indent=4, sort_keys=True))
        resString = "The next three buses to southpoint are coming at\n" 
        with open('1\stop_times.txt') as csvfile:
            #t = csvfile.read()
            stops = csv.DictReader(csvfile)
            l_t = localtime()
            counter = 0
            for row in stops:

                if int(row['stop_id']) == 203638:
                    a_tim = row['arrival_time']
                    if a_tim.startswith(str(24)):
                        #This means it has gone over and we need to look it around
                        a_tim = str(int(a_tim[:2])-24)+ a_tim[2:]
                        print(a_tim)
                    tm = strptime(row['arrival_time'], "%H:%M:%S")
                    if int(row['stop_id']) == 203638:
                        if tm.tm_hour >= l_t.tm_hour:
                            if tm.tm_min >= l_t.tm_min:
                                resString +=  "{0}\n".format(row['arrival_time'])
                                counter += 1
                                if counter == 2:
                                    break
            #resString = "Hello I am a potato"
        data = {
                    "payload": {
                        "google": {
                        "expectUserResponse": True,
                        "richResponse": {
                            "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": resString
                                }
                            }
                            ]
                        }
                        }
                    }
                }
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp
        #print(req_data)
    else:
        return "This is a webserver for the new potatos"