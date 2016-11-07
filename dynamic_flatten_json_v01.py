# version 0.1
# process that extracts all key value pairs from nested json data below
# "publication reference" level.

# CAVEAT: this process requires the data structure to start as follows:
# { "guid" :
#     "pubRef": [       // must be an array here
#         {...}                         // can put any valid json here
#     ]
# }

import json

def flattenDict(jDict, json):
    for item in jDict:
        if isinstance(jDict[item], (str, unicode)):
            json.update({item: jDict[item]})
        elif isinstance(jDict[item], dict):
            flattenDict(jDict[item], json)
        elif isinstance(jDict[item], list):
            flattenList(jDict[item], json)

def flattenList(jList, json):
    for item in range(len(jList)):
        if isinstance(jList[item], (str, unicode)):
            json.update({item: jList[item]})
        elif isinstance(jList[item], list):
            flattenList(jList[item], json)
        elif isinstance(jList[item], dict):
            flattenDict(jList[item], json)

with open("testJson/singleSample.json") as json_file:
    json_data = json.load(json_file)

    try:

        for guid in json_data:
            for pubRef in json_data[guid]:
                # creates a new json_output object for every "pubRef" item
                json_output = {"guid": guid}
                json_output.update({"pubRef": pubRef})

                # initiate conditional loops that will flatten nested data
                if isinstance(json_data[guid][pubRef], list):
                    flattenList(json_data[guid][pubRef], json_output)
    except:
        json_output = {"error": "there was an error"}

            print(json.dumps(json_output, indent=4, sort_keys=True))
            #print_xml_stream(json_output)
