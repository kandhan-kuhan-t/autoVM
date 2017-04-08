import redis
import pickle
import uuid

conn = redis.StrictRedis(host='localhost',port=2346)

def createRequest(obj):
    old = conn.get('requests')
    if old!=None:
        oldArray = pickle.loads(old)
    else:
        return -1
    _id = uuid.uuid4()
    obj['_id'] = _id
    oldArray.append(obj)
    conn.set('requests',pickle.dumps(oldArray))
    print('Request saved!')
    return 1

def getRequests():
    return pickle.loads(conn.get('requests'))

def getRequestById(id):
    requests = pickle.loads(conn.get('requests'))
    print(requests[0]['_id'])
    filtered = list(filter(lambda x:x['_id']==str(id),requests))
    if(len(filtered)==1):
        return filtered[0]
    else:
        return -1

def initRequest():
    conn.set('requests',pickle.dumps([]))
    return 1

if __name__ == '__main__':
    TEST = True
    if(TEST):
        initRequest()