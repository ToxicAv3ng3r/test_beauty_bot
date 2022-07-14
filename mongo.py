from datetime import datetime, timedelta
import time

import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client['test']
collection = current_db['users']
user = {
    'name': 'Nancy',
    'expired_at': datetime.now() + timedelta(hours=24)
}
collection.insert_one(user)


def del_expired_doc():
    while True:
        try:
            collection.delete_many({'expired_at': {"$lt": datetime.now()}})
            for user in collection.find():
                print(user)
            time.sleep(3600)
        except Exception as e:
            print(e)
            time.sleep(3600)


del_expired_doc()



