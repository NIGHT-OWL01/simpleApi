import requests
import json

URL="http://127.0.0.1:8000/carApi"



def get_data(id=None):
    data={}
    if id:
        data={'id':id}

    json_data=json.dumps(data)
    r= requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
get_data()

def save_data():
    data={
        'name':'nano',
        'price':100000,
        'date_of_purchase':'2002-11-12'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    res=r.json()
    print(res)
 #   save_data()

def update_data():
    data={
        'id':1,
        'name':'lamborgani',
     
        'date_of_purchase':'2021-01-15'
    }

    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    res=r.json()
    print(res)

#update_data()

def delete_data():
    data={'id':5}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    res=r.json()
    print(res)

#delete_data()








##play with Api
import random
random.randrange(100,400000)
name='rat'
price=1000
date='2000-1-11'
def create_data():
    data={
        'name':name,
        'price':price,
        'date_of_purchase':date
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    res=r.json()
    print(res)

#create_data()


#for i in range(10):

#    print('sent')