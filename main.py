# Import necessary functions
from helper_functions import *
from json_templates import *
from api_calls import *
import json

def main():
    try:
        # Grab DID, EID, and WVMID from Part Studio URL
        part_studio_URL = "https://cad.onshape.com/documents/0af072a8e59166eb73f43a08/w/9488cf7048fca2b0c3be8189/e/39b8de68e0b8abef3cdb7967" # Change this
        WVM = "w"
        DID, EID, WVMID = get_ids(part_studio_URL, WVM)

        # Generate JSON for circle sketch on Front plane
        sketch_json = get_sketch_json(radius=0.005, x=0.05, y=0.05, name="Parts Sketch")

        # Create circle sketch
        response = add_feature_to_partstudio(DID, WVM, WVMID, EID, sketch_json)

        # Get Feature ID
        feature_id = response.json()["feature"]["featureId"]
        print(f"New sketch ID: {feature_id}")

        # Generate extrusion JSON
        extrude_json = get_extrude_json(feature_id, depth=0.040, region_index=0)

        # Create extrusion
        response = add_feature_to_partstudio(DID, WVM, WVMID, EID, extrude_json)

        # Generate extrusion JSON
        extrude_json = get_extrude_json(feature_id, depth=0.040, region_index=1)

        # Create extrusion
        response = add_feature_to_partstudio(DID, WVM, WVMID, EID, extrude_json)
        
        # Get parts list and partId of most recent part
        parts_response = get_parts_list(DID, WVM, WVMID, EID)
        recent_parts = parts_response.json()[-2:]
        # partId = parts_response.json()[-1]['partId']
        # print(f"New part ID: {partId}")

        # Create new assembly
        assem_response = create_assembly(DID, WVM, WVMID, "My Assembly")
        assemEID = assem_response.json()['id']
        print(f"New assembly ID: {assemEID}")

        # Add part to assembly    
        for part in recent_parts:
            partId = part['partId']
            add_part_to_assembly(DID, WVM, WVMID, assemEID, EID, partId)
            assembly_definition = get_assembly_definition(DID, WVM, WVMID, assemEID)
        
            deterministicId1 = get_deterministic_id(assembly_definition, partId)
            print(f"New assembly path ID: {deterministicId1}")

            # Get the body details of the new part then find the top face
            body_details = get_body_details(DID, WVM, WVMID, EID, partId)
            faceId = get_face_id(body_details, 'y', 0.0)
            print(f"New part face ID: {faceId}")

            # Generate JSON for new mate connector
            mate_connector_json = get_mate_connector_json(deterministicId1, faceId)

            # Create new mate connector on part
            mc_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_connector_json)
            mc_id = mc_response.json()['feature']['featureId']
            print(f"New mate connector ID: {mc_id}")

        # # Generate JSON for new mate connector at origin
        # origin_json = get_origin_json()

        # # Create new mate connector at origin
        # origin_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, origin_json)
        # mc_origin_id = origin_response.json()['feature']['featureId']
        # print(f"New mate connector at origin ID: {mc_origin_id}")

        # # Generate JSON for new fastened mate
        # mate_json = get_mate_json(mc_id, mc_origin_id, "FASTENED", False)

        # # Create new fastened mate in assembly
        # add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_json)

        # # Get part ID from existing part
        # existingEID = get_existing_eid(DID, WVM, WVMID)
        # parts_response = get_parts_list(DID, WVM, WVMID, existingEID)
        # existing_partId = parts_response.json()[-1]['partId']
        # print(f"Existing part ID: {existing_partId}")

        # # Add part to assembly    
        # add_part_to_assembly(DID, WVM, WVMID, assemEID, existingEID, existing_partId)
        # assembly_definition = get_assembly_definition(DID, WVM, WVMID, assemEID)
        # deterministicId2 = get_deterministic_id(assembly_definition, existing_partId)
        # print(f"New assembly path ID: {deterministicId2}")

        # # Get the body details of the new part
        # body_details = get_body_details(DID, WVM, WVMID, existingEID, existing_partId)
        # faceId = get_face_id(body_details, 'x', 0.0)
        # print(f"New part face ID: {faceId}")

        # # Generate JSON for new mate connector
        # mate_connector_json = get_mate_connector_json(deterministicId2, faceId)

        # # Create new mate connector on part
        # mc_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_connector_json)
        # mc_id2 = mc_response.json()['feature']['featureId']
        # print(f"New mate connector ID: {mc_id2}")

        # # Generate JSON for new revolute mate
        # mate_json = get_mate_json(mc_id, mc_id2, "REVOLUTE", False)

        # # Create new revolute mate in assembly
        # add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_json)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
