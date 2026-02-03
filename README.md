# api-assembly-exercises

## Code Flow

These steps are executed sequentially in main.py.  Just run

`python3 main.py`

* Sketch a circle
* Get the sketch's feature ID
* Extrude the circle
* Get the cylinder's part ID
* Create a new assembly
* Insert the cylinder into the new assembly
* Get the face ID for the cylinder's top face
* Add Mate Connector to face
* Add Mate Connector to Origin
* Create Fastened mate
* Get element and part ID for existing part
* Add existing part to assembly
* Get the face ID for the part's bottom face
* Add Mate Connector to face
* Create Revolute mate

## File Structure
```
api-assembly-exercises/
├── main.py              # Main script
├── APIKey.json          # Your Onshape API Keys.  Don't share!
├── api_calls.py         # API functions (GET, POST, etc.)
├── json_templates.py    # Functions that return JSON structures
└── helper_functions.py  # Python functions 
```