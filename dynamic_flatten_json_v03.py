# version 0.3
# process that extracts all key value pairs from nested json data below
# "publication reference" level.

# CAVEAT: this process requires the data structure to start as follows:
# { "guid" :
#     "pubRef": [       // must be an array here
#         {...}                         // can put any valid json here
#     ]
# }

# v0.2
# accounts for each "publication reference" to contain multiple "edits"

# v03
# add functionality that caters for muliple instruments and flattens them

import json

def flattenDict(jDict, json):
    for item in jDict:
        if isinstance(jDict[item], (str, unicode)):
            json.update({item: jDict[item]})

        # new loop that checks whether the key is "instruments" and the value is a "list"
        elif item == "instruments" and isinstance(jDict[item], list):

            # an nested loop that iterates through each instrument in the list
            for instruments in range(len(jDict[item])):

                # create empty placeholder object that will contain the flattened instrument blob
                flatInstrument = {}

                # use the existing flattenDict() function to populate the placeholder object
                flattenDict(jDict[item][instruments],flatInstrument)

                # appy the flattened instrument blob into the json object that will be sent to splunk
                json[item].append(flatInstrument)

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

    # iterates through each guid
    for guid in json_data:

        #iterates through each publication referernce corresponding to the guid
        for pubRef in json_data[guid]:

            # iterates through each edit in the publication reference array
            for edits in range(len(json_data[guid][pubRef])):

                # creates a new json_output object for every edit blob
                json_output = {"guid": guid}
                json_output.update({"pubRef": pubRef})

                # create an empty list inside the object that will contain the flattened instrument blobs
                json_output.update({"instruments": []})

                # initiate conditional loops that will flatten nested data
                flattenDict(json_data[guid][pubRef][edits], json_output)

                ### Do stuff related to "lastModifiedDate" field

                print(json.dumps(json_output, indent=4, sort_keys=True))
                #print_xml_stream(json_output)
