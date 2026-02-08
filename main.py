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
        
        # Globals
        XOFFSET = 0.01
        R1 = 0.005
        R2 = 0.02

        # Generate JSON for two circles on Front plane
        sketch_json = get_sketch_json(r1=R1, r2=R2, xOffset=XOFFSET, yOffset=0.0, name="Parts Sketch")

        # Create circle sketch
        response = add_feature_to_partstudio(DID, WVM, WVMID, EID, sketch_json)

        # Get Feature ID
        feature_id = response.json()["feature"]["featureId"]
        print(f"New sketch ID: {feature_id}")

        for i in range(2):
            # Generate extrusion JSON for region
            extrude_json = get_extrude_json(feature_id, depth=0.040, region_index=i)

            # Create extrusion
            response = add_feature_to_partstudio(DID, WVM, WVMID, EID, extrude_json)
        
        # Get parts list and partId for two most recent parts
        parts_response = get_parts_list(DID, WVM, WVMID, EID)
        recent_parts = parts_response.json()[-2:]

        # Create new assembly
        assem_response = create_assembly(DID, WVM, WVMID, "My Assembly")
        assemEID = assem_response.json()['id']
        print(f"New assembly ID: {assemEID}")
        part_mcs = []

        # Add both parts to assembly and add mate connectors
        for i, part in enumerate(recent_parts):
            partId = part['partId']
            add_part_to_assembly(DID, WVM, WVMID, assemEID, EID, partId)
            assembly_definition = get_assembly_definition(DID, WVM, WVMID, assemEID)
        
            deterministicId = get_deterministic_id(assembly_definition, partId)
            print(f"New assembly path ID: {deterministicId}")

            # Get the body details of the new part then find the top face
            body_details = get_body_details(DID, WVM, WVMID, EID, partId)
            faceId = get_face_id(body_details, 'y', 0.0)
            print(f"New part face ID: {faceId}")

            # Generate JSON for new mate connector
            if i == 1:
                centroidOffset = get_centroid_offset(R1, R2)
            else:
                centroidOffset = 0
            mate_connector_json = get_mate_connector_json(deterministicId, faceId, centroidOffset)

            # Create new mate connector on part
            mc_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_connector_json)
            mc_id = mc_response.json()['feature']['featureId']
            part_mcs.append(mc_id)
            print(f"New mate connector ID: {mc_id}")

        # Generate JSON for new mate connector at origin
        origin_json = get_origin_json()

        # Create new mate connector at origin
        origin_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, origin_json)
        mc_origin_id = origin_response.json()['feature']['featureId']
        print(f"New mate connector at origin ID: {mc_origin_id}")

        # Generate JSON for new fastened mate
        mate_json = get_mate_json(part_mcs[0], mc_origin_id, "FASTENED", False)

        # Create new fastened mate in assembly
        mate_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_json)
        mate_id = mate_response.json()['feature']['featureId']
        print(f"New mate ID: {mate_id}")

        # Generate JSON for new revolute mate
        mate_json = get_mate_json(part_mcs[0], part_mcs[1], "REVOLUTE", False)

        # Create new revolute mate in assembly
        mate_response = add_feature_to_assembly(DID, WVM, WVMID, assemEID, mate_json)
        mate_id = mate_response.json()['feature']['featureId']
        print(f"New mate ID: {mate_id}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
