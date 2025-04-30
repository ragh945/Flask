##Put and delete HTTP-Verbs
## Working with API'S-->Json's

from flask import Flask, jsonify, request,render_template,redirect,url_for,flash,session

app=Flask(__name__)

##Initial data into my list
items=[{"id":1,"name":"Item 1","description":"This is item1"},
{"id":2,"name":"Item 2","description":"This is item2"}]

@app.route("/")
def welcome():
    return "Welcome to the Flask Application!"

## GET: Retrieve all the elements from the list
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

## GET: Retrieve a single element from the list
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error":"Item not found"})

##POST: Create a new task
@app.route("/items",methods=["POST"])
def create_item():
         if not request.json or not "name" in request.json:
                return jsonify({"error":"Bad Request"}),400
         new_item={
        "id":items[-1]["id"]+1,
        "name":request.json["name"],
        "description":request.json["description"]
    
    }
         items.append(new_item)
         return jsonify(new_item)

#PUT: Update an existing task
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item:
        if not request.json:
            return jsonify({"error":"Bad Request"}),400
        item["name"]=request.json.get("name",item["name"])
        item["description"]=request.json.get("description",item["description"])
        return jsonify(item)
    else:
        return jsonify({"error":"Item not found"})


#DELETE: Delete an existing task
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item:
        items.remove(item)

        return jsonify({"message":"Item deleted successfully"})
    else:
        return jsonify({"error":"Item not found"})





if __name__=="__main__":
    app.run(debug=True) #debug=True will reload the server when you make changes to the code.