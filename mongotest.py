from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://skapiec.4ju5ocq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Skapiec"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./certs/X509-cert-3621885173140152299.pem',
                     server_api=ServerApi('1'))
db = client['Skapiec']
collection = db['Skapiec']
doc_count = collection.count_documents({})
print(doc_count)