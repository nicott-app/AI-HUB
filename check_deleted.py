import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()
cred = credentials.Certificate("./firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

tickets = db.collection("projects").document("timecare").collection("tickets").stream()
print("Tickets en Timecare:")
for t in tickets:
    data = t.to_dict()
    print(f"[{t.id}] ID: {data.get('id')} | Titulo: {data.get('title')[:30]} | Status: {data.get('status')} | Archived: {data.get('archived')} | isDeleted: {data.get('isDeleted')}")
