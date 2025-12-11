import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
client.admin.command("ping")
db = client['test_database']

stack1 = {
  'name': 'customer1',
  'pip': ['pyhton', 'java', 'go'],
  'info': {'os': 'mac' },
  'data': datetime.datetime.utcnow()
}

stack2 = {
  'name': 'customer2',
  'pip': ['pyhton', 'java'],
  'info': {'os': 'windows' },
  'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
# stacks_id = db_stacks.insert_one(stack1).inserted_id
# print(stacks_id, type(stacks_id))
# print('####################')
# from bson.objectid import ObjectId
# str_stacks_id = ObjectId('68fd8736ccf53443d92d9a8a')
# print(db_stacks.find_one({'_id': ObjectId(str_stacks_id)}))
# print(db_stacks.find_one({'pip': []}))
# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# for stack in db_stacks.find():
#   print(stack)
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$lt': now}}):
  print(stack)