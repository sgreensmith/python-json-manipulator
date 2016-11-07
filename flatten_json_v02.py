# version 0.2
# added a json parser function to validate the format of the output

import json

with open("testJson/singleSample.json") as json_file:
    json_data = json.load(json_file)

    flat_json = ""

    for guid in json_data:

        for docRef in json_data[guid]:

            # acknowledgements
            hasRecommendation = json_data[guid][docRef][0]["acknowledgements"]["hasRecommendation"]
            conflictOfInterest = json_data[guid][docRef][0]["acknowledgements"]["conflictOfInterest"]
            adheresToInvestmentRecommendationsPolicy = json_data[guid][docRef][0]["acknowledgements"]["adheresToInvestmentRecommendationsPolicy"]

            # instruments
            instrumentReferenceKey = json_data[guid][docRef][0]["instruments"][0]["instrumentReferenceKey"]
            recommendation = json_data[guid][docRef][0]["instruments"][0]["recommendation"]
            timeHorizon = json_data[guid][docRef][0]["instruments"][0]["timeHorizon"]
            assetClass = json_data[guid][docRef][0]["instruments"][0]["assetClass"]

            # instrumentIdentifiers
            symbol = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["symbol"]
            cusip = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["cusip"]
            issueName = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["issueName"]
            bbTicker = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["bbTicker"]
            description = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["description"]
            sedol = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["sedol"]
            ric = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["ric"]
            masterId = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["masterId"]
            instrumentName = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["instrumentName"]
            nonCompositeBbTicker = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["nonCompositeBbTicker"]
            currency = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["currency"]
            exchange = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["exchange"]
            countryOfListing = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["countryOfListing"]
            ubsId = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["ubsId"]
            isin = json_data[guid][docRef][0]["instruments"][0]["instrumentIdentifiers"]["isin"]

            # other meta data
            articleId = json_data[guid][docRef][0]["articleId"]
            lastModifiedDate = json_data[guid][docRef][0]["lastModifiedDate"]
            deleted = json_data[guid][docRef][0]["deleted"]

            try:
                new_data = json_data[guid][docRef][0]["new_data"]
            except:
                new_data = "++++++++++++++++++++++++++++++"


            # append object corresponding to document reference to the output string
            # NB: have to manually append a 'comma' to the end of the object (the final comma will have to be manually removed)
            flat_json += json.dumps({"GUID": guid,
                                    "docRef": docRef,
                                    "hasRecommendation": hasRecommendation,
                                    "conflictOfInterest": conflictOfInterest,
                                    "adheresToInvestmentRecommendationsPolicy": adheresToInvestmentRecommendationsPolicy,
                                    "instrumentReferenceKey": instrumentReferenceKey,
                                    "recommendation": recommendation,
                                    "timeHorizon": timeHorizon,
                                    "assetClass": assetClass,
                                    "symbol": symbol,
                                    "cusip": cusip,
                                    "issueName": issueName,
                                    "bbTicker": bbTicker,
                                    "description": description,
                                    "sedol": sedol,
                                    "ric": ric,
                                    "masterId": masterId,
                                    "instrumentName": instrumentName,
                                    "nonCompositeBbTicker": nonCompositeBbTicker,
                                    "currency": currency,
                                    "exchange": exchange,
                                    "countryOfListing": countryOfListing,
                                    "ubsId": ubsId,
                                    "isin": isin,
                                    "articleId": "articleId",
                                    "lastModifiedDate": lastModifiedDate,
                                    "deleted": deleted,
                                    "new_data": new_data
                                    }, sort_keys=True, indent=4) + ','

# the following removes the last comma to ensure output is valid json
flat_json = '[' + flat_json[:-1] + ']'
parsed_json = json.loads(flat_json)

print(json.dumps(parsed_json, indent=4))
