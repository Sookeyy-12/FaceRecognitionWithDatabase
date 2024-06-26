import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://demofacerecognition-77f12-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference("Students")

data = {
    'Suket': 
        {
            'name' : 'Suket Kamboj',
            'major': 'CSE',
            'startingYear': 2022,
            'total_attendance': 7,
            'year': 3,
            'last_attendance_time': "2022-06-20 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)