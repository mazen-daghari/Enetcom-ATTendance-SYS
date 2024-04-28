
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': " ",
})
ref = db.reference('Mahasiswa')

data = {
    "200103112":
        {
            "nama": "Mazen ",
            "jurusan": "TI",
            "angkatan": "2020",
            "total_attendance": 0,
            "status": "mhs",
            "tahun": 2,
            "last_attendance_time": "2022-12-24 18:30:00"
        }
}


for key, value in data.items():
    ref.child(key).set(value)