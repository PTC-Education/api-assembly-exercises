import math 

def get_ids(url, wv):
    urlArr = url.split("/")
    dIndex = urlArr.index("documents")
    DID = urlArr[dIndex + 1]
    eIndex = urlArr.index("e")
    EID = urlArr[eIndex + 1]
    wvIndex = urlArr.index(wv)
    WVID = urlArr[wvIndex + 1]

    return DID, EID, WVID

def get_instance_id(definition, partId):
    json = definition.json()
    for instance in json['rootAssembly']['instances']:
            if instance['partId'] == partId:
                instanceId = instance['id']
    return instanceId    

def get_face_id(body_details, axis, location):
    bodies = body_details.json()['bodies']
    for face in bodies[0]['faces']:
        surface = face['surface']
        if surface['type'] == 'PLANE':
            origin = surface['origin']
            if abs(origin[axis] - location) < 1e-6:
                faceId = face['id']
    return faceId

def get_centroid_offset(r1, r2, xOffset):
     A1 = math.pi * r1**2
     A2 = math.pi * r2**2
     centroid_offset = -(A2 * xOffset) / (A2 - A1)
     return centroid_offset