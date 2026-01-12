from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }
    collection.insert_one(data)
    return {"message": "Item stored successfully"}
