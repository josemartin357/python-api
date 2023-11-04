import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# sample data 
# in dictionary, the id is set automatically with first value
data = {
    "1": {"name": "Alice", "description": "A software engineer"},
    "2": {"name": "Bob", "description": "A data analyst"},
    "3": {"name": "Charlie", "description": "A graphic designer"},
    "4": {"name": "David", "description": "A marketing specialist"},
    "5": {"name": "Eve", "description": "A project manager"},
}

# class instance to handle HTTP requests
class APIServer(BaseHTTPRequestHandler):
    # setting HTTP response headers
    def _set_response(self, status_code=200, content_type="application/json"): 
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    # handle GET requests
    def do_GET(self):
        if self.path == "/api/items":  # path to respond all items
            self._set_response()  # setting response headers
            self.wfile.write(json.dumps(data).encode())  # write json response
        elif self.path.startswith("/api/item/"):  # path for a single item
            item_id = self.path.split("/api/item/")[1]  # splitting to get item_id
            item = data.get(item_id) # getting item with item_id
            if item:
                self._set_response()  # set response headers
                self.wfile.write(json.dumps(item).encode())  # write json response
            else:
                self._set_response(404)  # 404 status code if item not found
        else:
            self._set_response(404)  # 404 status code for other paths

    # handle POST requests
    def do_POST(self):
        if self.path == "/api/items": # checking path
            content_length = int(self.headers["Content-Length"]) # getting content length from request headers
            post_data = self.rfile.read(content_length) # read post data from request
            new_item = json.loads(post_data) # parse JSON data from request
            new_id = str(len(data) + 1) # generate id for new item
            data[new_id] = new_item  # add new item to data 
            self._set_response(201)  # set http response with 201 (Created)
            self.wfile.write(new_id.encode())  # write new item as the response body
        else:
            self._set_response(404) # 404 status code for other paths


    # handle PUT requests
    def do_PUT(self):
        if self.path.startswith("/api/item/"): # checking path
            item_id = self.path.split("/api/item/")[1] # getting item_id from path
            if item_id in data: # checking if item_id exists
                content_length = int(self.headers["Content-Length"]) # getting content length
                put_data = self.rfile.read(content_length) # read data
                updated_item = json.loads(put_data) # parse data
                data[item_id] = updated_item # updating item_id with new data
                self._set_response(204)  # respond 204 for successful update
            else:
                self._set_response(404)  # respond 404 if item is not found
        else:
            self._set_response(404)  # 404 status code for other paths

    # handle DELETE requests
    def do_DELETE(self):
        if self.path.startswith("/api/item/"): # checking path
            item_id = self.path.split("/api/item/")[1] # getting item_id from path
            if item_id in data: # if item exists
                del data[item_id] # delete item from data dict
                self._set_response(204)  # respond 204 status code for successful deletion
            else:
                self._set_response(404)  # 404 status code if item is not found
        else:
            self._set_response(404)  # 404 status code for other paths

# function starts HTTP server.
def run(server_class=HTTPServer, handler_class=APIServer, port=8000):
    server_address = ("", port) # create server address w/empty tuple and port 8000
    httpd = server_class(server_address, handler_class) # create instance of the specified server class 
    print(f"Starting server on port {port}")

    httpd.serve_forever() # Start http server

# if script run as main program ...
if __name__ == "__main__":
    # ... run it and start server
    run()

