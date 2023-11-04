# python-api
This is a personal refresher on how APIs are built with Python. For this project, I am only using the Python modules; not frameworks.
A future update to this project will include authorization and other features.

## To run

In Root folder of this repo, run `python api.py` in your Terminal. That will initiate the server and you will see the message `Starting server on port 8000`.

## Example of API calls using Curl

**GET**

`curl http://localhost:8000/api/items`

`curl http://localhost:8000/api/item/1`

**POST**

`curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "description": "A cool dude"}' http://localhost:8000/api/items`

**PUT**

`curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item 3", "description": "This is the updated item 3"}' http://localhost:8000/api/item/3`

**DELETE**

`curl -X DELETE http://localhost:8000/api/item/3`
