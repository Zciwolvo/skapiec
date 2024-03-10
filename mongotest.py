from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://skapiec.4ju5ocq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Skapiec"
certificate_file = './certs/X509-cert-3621885173140152299.pem'


def read_from_mongodb(collection_name):
    # Get the collection
    collection = db[collection_name]
    # Query all documents from the collection excluding the _id field
    documents = collection.find({}, {'_id': 0})
    # Convert documents to JSON
    json_data = [doc for doc in documents]
    return json_data



def write_to_mongodb(collection_name, json_data):
    # Get the collection
    collection = db[collection_name]
    # Insert JSON data into the collection
    collection.insert_many(json_data)
    
    
client = MongoClient(uri, tls=True, tlsCertificateKeyFile=certificate_file, server_api=ServerApi('1'))
db = client.get_database("Skapiec")


def delete_records_by_category(collection_name, category):
    # Get the collection
    collection = db[collection_name]
    # Delete documents with the specified category
    result = collection.delete_many({"category": category})
    # Return the number of deleted documents
    return result.deleted_count


delete_records_by_category("skapiec", "Electronics")

