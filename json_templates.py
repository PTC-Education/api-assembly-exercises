def get_sketch_json(radius, x, y, name):
    return {
  "feature" : {
    "btType": "BTMSketch-151", 
    "featureType": "newSketch", 
    "name": name, 
    "parameters": [
      {
        "btType": "BTMParameterQueryList-148",
        "queries": [
          {
            "btType": "BTMIndividualQuery-138",
            "queryString": "query=qCreatedBy(makeId(\"Front\"), EntityType.FACE);"
          }
        ],
        "parameterId": "sketchPlane" 
      }
    ],
    "entities": [
      {
        "btType": "BTMSketchCurve-4",
        "geometry": {
          "btType": "BTCurveGeometryCircle-115",
          "radius": radius*2,  
          "xCenter": x,
          "yCenter": y,  
          "xDir": 1,
          "yDir": 0, 
          "clockwise": False 
        },
        "centerId": "big-circle.center",
        "entityId": "big-circle"
      },
      {
        "btType": "BTMSketchCurve-4",
        "geometry": {
          "btType": "BTCurveGeometryCircle-115",
          "radius": radius,  
          "xCenter": x+.001,
          "yCenter": y,  
          "xDir": 1,
          "yDir": 0, 
          "clockwise": False 
        },
        "centerId": "small-circle.center",
        "entityId": "small-circle"
      }    
    ],
    "constraints": [      
    ]
  }
}

def get_extrude_json(feature_id, depth, region_index):
    return {
          "btType": "BTFeatureDefinitionCall-1406",
          "feature": {
            "btType": "BTMFeature-134",
            "featureType": "extrude",
            "name": "Extrude 1",
            "parameters": [
              {
                "btType": "BTMParameterEnum-145",
                "value": "SOLID",
                "enumName": "ExtendedToolBodyType",
                "parameterId": "bodyType"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "NEW",
                "enumName": "NewBodyOperationType",
                "parameterId": "operationType"
              },
              {
                "btType": "BTMParameterQueryList-148",
                "queries": [
                  {
                    "btType": "BTMIndividualQuery-138",
                    "queryString": f'query=qNthElement(qSketchRegion(makeId("{feature_id}"), false), {region_index});'
                  }
                ],
                "parameterId": "entities"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "BLIND",
                "enumName": "BoundingType",
                "parameterId": "endBound"
              },
              {
                "btType": "BTMParameterQuantity-147",
                "expression": str(depth) + " m",
                "parameterId": "depth"
              }
                ],
            "returnAfterSubfeatures": False,
            "suppressed": False
          }
        }

def get_mate_connector_json(instanceID, deterministicId):
    return {
        "feature": {    
            "btType": "BTMMateConnector-66",
            "featureType": "mateConnector",
            "name": "Mate connector 1",
            "parameters": [
                {
                  "btType": "BTMParameterEnum-145",
                  "enumName": "Origin type",
                  "value": "ON_ENTITY",
                  "parameterId": "originType"
                },
                {
                  "btType": "BTMParameterQueryWithOccurrenceList-67",
                  "queries": [
                      {
                      "btType": "BTMInferenceQueryWithOccurrence-1083",
                      "inferenceType": "CENTROID",
                      "path": [
                          instanceID
                      ],
                      "deterministicIds": [
                          deterministicId
                      ]
                      }
                  ],
                  "parameterId": "originQuery",
                  "parameterName": "",
                  "libraryRelationType": "NONE"
                },
                {
                    "btType": "BTMParameterBoolean-144",
                    "value": True,
                    "parameterId": "transform"
                },
                {
                  "btType": "BTMParameterQuantity-147",
                  "expression": "0.01 m",
                  "parameterId": "translationX"
                }
            ],
            "isHidden": False,
            "suppressed": False
            }
        }

def get_origin_json():
    return {
    "feature": {
        "btType": "BTMMateConnector-66",
        "featureType": "mateConnector",
        "name": "Assembly Origin MC",
        "parameters": [
            {
                "btType": "BTMParameterEnum-145",
                "enumName": "Origin type",
                "value": "ON_ENTITY",
                "parameterId": "originType",
                "parameterName": ""
            },
            {
                "btType": "BTMParameterQueryWithOccurrenceList-67",
                "queries": [
                    {
                        "btType": "BTMFeatureQueryWithOccurrence-157",
                        "path": [],
                        "featureId": "Origin",
                        "queryData": "ORIGIN_Z"
                    }
                ],
                "parameterId": "originQuery",
                "parameterName": ""
            }
        ],
        "isHidden": False,
        "suppressed": False
    }
}

def get_mate_json(featureId1, featureId2, type, reorient):
    return {
    "feature": {
        "btType": "BTMMate-64",
        "featureType": "mate",
        "returnAfterSubfeatures": False,
        "subFeatures": [],
        "namespace": "",
        "version": 2,
        "name": "Fastened 1",
        "parameters": [
            {
            "btType": "BTMParameterEnum-145",
            "namespace": "",
            "enumName": "Mate type",
            "value": type,
            "parameterId": "mateType"
            },
            {
              "btType": "BTMParameterBoolean-144",
              "value": reorient,
              "nodeId": "8tlsPz/G1alBQ0HRcVTe7rMf",
              "parameterId": "primaryAxisAlignment",
              "parameterName": "",
              "libraryRelationType": "NONE"
            },
            {
            "btType": "BTMParameterQueryWithOccurrenceList-67",
            "queries": [
                {
                "btType": "BTMFeatureQueryWithOccurrence-157",
                "path": [],
                "featureId": featureId1,
                "queryData": ""
                },
                {
                "btType": "BTMFeatureQueryWithOccurrence-157",
                "path": [],
                "featureId": featureId2,
                "queryData": ""
                }
            ],
            "parameterId": "mateConnectorsQuery"
            }
        ],
        "suppressed": False
        }
    }
