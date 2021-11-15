import firebase_admin
import matplotlib.pyplot as plt
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account
cred = credentials.Certificate('roomeo-6acbb-3dff41e45b38.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

name = []
currentCap = []
occupation = []

    
docs = db.collection('Buildings').get()
for doc in docs:
    number = 0
    d = doc.to_dict()
    name.append(d['Name'])
    for classrooms in d['classrooms']:
        n = classrooms['currentCap']
        number = number + n
    percent = (number/d['Capacity'])*100
    occupation.append(percent)

plt.bar(name,occupation)
plt.title('Porcentaje de ocupación por edificios')
plt.xlabel('Edifios')
plt.ylabel('% de ocupación')
plt.show()