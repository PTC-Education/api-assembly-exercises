# api-assembly-exercises

## Code Flow

These steps are executed sequentially in main.py.  Just run

`python3 main.py`

* Sketch two circles
* Get the sketch's feature ID
* Extrude both circles
* Get the cylinder part IDs
* Create a new assembly
* Insert the cylinders into the new assembly
* Get face IDs for each cylinder's top face
* Add Mate Connector to each face
* Add Mate Connector to Origin
* Create Fastened mate between one cylinder and Origin
* Create Revolute mate between two cylinders

## File Structure
```
api-assembly-exercises/
├── main.py              # Main script
├── APIKey.json          # Your Onshape API Keys.  Don't share!
├── api_calls.py         # API functions (GET, POST, etc.)
├── json_templates.py    # Functions that return JSON structures
└── helper_functions.py  # Python functions 
```