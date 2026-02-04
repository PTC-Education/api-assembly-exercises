import requests
import json

with open("APIKey.json") as f:  # Change file name if needed
    data = json.load(f)
    API_ACCESS = data["access"]
    API_SECRET = data["secret"]

api_keys = (API_ACCESS, API_SECRET)
MEDIA_TYPE = "application/json;charset=UTF-8;qs=0.09"
headers = {"Accept": MEDIA_TYPE, "Content-Type": "application/json"}
baseURL = "https://cad.onshape.com/api/v13/"

def add_feature_to_partstudio(DID, WVM, WVMID, EID, json_data):    
    apiURL = "partstudios/d/{}/{}/{}/e/{}/features/".format(DID, WVM, WVMID, EID)
    URL = baseURL + apiURL
    response = requests.post(URL, auth=api_keys, headers=headers, json=json_data)
    return response

def add_feature_to_assembly(DID, WVM, WVMID, EID, json_data):    
    apiURL = "assemblies/d/{}/{}/{}/e/{}/features/".format(DID, WVM, WVMID, EID)
    URL = baseURL + apiURL
    response = requests.post(URL, auth=api_keys, headers=headers, json=json_data)
    return response

def create_assembly(DID, WVM, WVMID, assem_name):
    apiURL = "assemblies/d/{}/{}/{}".format(DID, WVM, WVMID)
    URL = baseURL + apiURL
    json_data = {
        "name": assem_name
    }
    response = requests.post(URL, auth=api_keys, headers=headers, json=json_data)
    return response

def get_parts_list(DID, WVM, WVMID, EID):
    apiURL = "parts/d/{}/{}/{}/e/{}".format(DID, WVM, WVMID, EID)
    URL = baseURL + apiURL
    response = requests.get(URL, auth=api_keys, headers=headers)
    return response

def add_part_to_assembly(DID, WVM, WVMID, targetEID, sourceEID, partId):
    apiURL = "assemblies/d/{}/{}/{}/e/{}/instances".format(DID, WVM, WVMID, targetEID)
    URL = baseURL + apiURL
    json_data = {
        "documentId": DID,
        "elementId": sourceEID,
        "includePartTypes": [
            "PARTS"
        ],
        "partId": partId
    }
    response = requests.post(URL, auth=api_keys, headers=headers, json=json_data)
    return response

def get_assembly_definition(DID, WVM, WVMID, EID):
    apiURL = "assemblies/d/{}/{}/{}/e/{}".format(DID, WVM, WVMID, EID)
    URL = baseURL + apiURL
    response = requests.get(URL, auth=api_keys, headers=headers)
    return response

def get_body_details(DID, WVM, WVMID, EID, partId):
    apiURL = "parts/d/{}/{}/{}/e/{}/partid/{}/bodydetails".format(DID, WVM, WVMID, EID, partId)
    URL = baseURL + apiURL
    response = requests.get(URL, auth=api_keys, headers=headers)
    return response

def get_existing_eid(DID, WVM, WVMID):
    apiURL = "documents/d/{}/{}/{}/elements".format(DID, WVM, WVMID)
    URL = baseURL + apiURL
    response = requests.get(URL, auth=api_keys, headers=headers)
    for element in response.json():
        if element['name'] != "Part Studio 1" and element['elementType'].lower() == "partstudio":
            return element['id']
    
    # If no matching element found
    raise ValueError("No extra Part Studio Found")