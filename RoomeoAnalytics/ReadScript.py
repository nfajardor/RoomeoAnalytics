import firebase_admin
import matplotlib.pyplot as plt
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account
cred = credentials.Certificate('roomeo-6acbb-3dff41e45b38.json')


db = firestore.client()

name = []
maxCap = []
currentCap = []
occupation = []

    
docs = db.collection('Buildings').get()
for doc in docs:
    number = 0
    d = doc.to_dict()
    name.append(d['Name'])
    maxCap.append(d['Capacity'])
    for classrooms in d['classrooms']:
        n = classrooms['currentCap']
        number = number + n
    currentCap.append(number)


print(name)
print(maxCap)
print(currentCap)

plt.bar(name,currentCap)
plt.title('Porcentaje de ocupación por edificios')
plt.xlabel('Edifios')
plt.ylabel('% de ocupación')
plt.show()