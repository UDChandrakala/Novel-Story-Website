import pymongo

client = pymongo.MongoClient("mongodb+srv://ugranamchandrakala23_db_user:novels123@kasv-cluster.iqwvnkh.mongodb.net/novels_db?retryWrites=true&w=majority&tls=true")
print(client.list_database_names())
