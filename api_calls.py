import requests
import json

with open("APIKey.json") as f:  # Change file name if needed
    data = json.load(f)
    API_ACCESS = data["access"]
    API_SECRET = data["secret"]

api_keys = (API_ACCESS, API_SECRET)
MEDIA_TYPE = "application/json;charset=UTF-8;qs=0.09"
headers = {"Accept": MEDIA_TYPE, "Content-Type": "application/json"}
base_url = "https://cad.onshape.com/api/v13/"

def add_feature_to_partstudio(DID, WVM, WVMID, EID, json_data):    
    api_url = "partstudios/d/{}/{}/{}/e/{}/features/".format(DID, WVM, WVMID, EID)
    url = base_url + api_url
    response = requests.post(url, auth=api_keys, headers=headers, json=json_data)
    return response

def add_feature_to_assembly(DID, WVM, WVMID, EID, json_data):    
    api_url = "assemblies/d/{}/{}/{}/e/{}/features/".format(DID, WVM, WVMID, EID)
    url = base_url + api_url
    response = requests.post(url, auth=api_keys, headers=headers, json=json_data)
    return response

def create_assembly(DID, WVM, WVMID, assem_name):
    api_url = "assemblies/d/{}/{}/{}".format(DID, WVM, WVMID)
    url = base_url + api_url
    json_data = {
        "name": assem_name
    }
    response = requests.post(url, auth=api_keys, headers=headers, json=json_data)
    return response

def get_parts_list(DID, WVM, WVMID, EID):
    api_url = "parts/d/{}/{}/{}/e/{}".format(DID, WVM, WVMID, EID)
    url = base_url + api_url
    response = requests.get(url, auth=api_keys, headers=headers)
    return response

def add_part_to_assembly(DID, WVM, WVMID, targetEID, sourceEID, partId):
    api_url = "assemblies/d/{}/{}/{}/e/{}/instances".format(DID, WVM, WVMID, targetEID)
    url = base_url + api_url
    json_data = {
        "documentId": DID,
        "elementId": sourceEID,
        "includePartTypes": [
            "PARTS"
        ],
        "partId": partId
    }
    response = requests.post(url, auth=api_keys, headers=headers, json=json_data)
    return response

def get_assembly_definition(DID, WVM, WVMID, EID):
    api_url = "assemblies/d/{}/{}/{}/e/{}".format(DID, WVM, WVMID, EID)
    url = base_url + api_url
    response = requests.get(url, auth=api_keys, headers=headers)
    return response

def get_body_details(DID, WVM, WVMID, EID, partId):
    api_url = "parts/d/{}/{}/{}/e/{}/partid/{}/bodydetails".format(DID, WVM, WVMID, EID, partId)
    url = base_url + api_url
    response = requests.get(url, auth=api_keys, headers=headers)
    return response
