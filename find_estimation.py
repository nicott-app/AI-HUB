import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()
cred = credentials.Certificate("./firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

projects = ["data-ia", "timecare"]
for p in projects:
    print(f"Project: {p}")
    # Also get the project document to see if it holds a counter prefix
    proj_doc = db.collection("projects").document(p).get()
    print("Project Data:", proj_doc.to_dict())
    
    tickets = db.collection("projects").document(p).collection("tickets").stream()
    for t in tickets:
        data = t.to_dict()
        keys = list(data.keys())
        time_keys = [k for k in keys if "time" in k.lower() or "estim" in k.lower() or "hour" in k.lower() or "day" in k.lower()]
        if time_keys:
            print(f"Ticket {t.id} has time fields: {time_keys}")
            for k in time_keys:
                print(f"  {k}: {data[k]}")
