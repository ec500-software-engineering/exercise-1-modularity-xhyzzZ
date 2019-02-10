import pymongo
from bson import ObjectId

#connect database
connection = pymongo.MongoClient("localhost", 27017)

#create database
database = connection['my_database']

#create collection
collection = database['my_collection']


def insert(data):
    document = collection.insert_one(data)
    return document.inserted_id

def update_or_create(document_id, data):
    document = collection.delete_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged

def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged

def get_single_data(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_mutiple_data(document_id):
    data = collection.find()
    return list(data)

connection.close()