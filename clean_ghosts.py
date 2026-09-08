import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()
cred = credentials.Certificate("./firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

projects = ["timecare", "data-ia"]
deleted_count = 0

for p in projects:
    tickets = db.collection("projects").document(p).collection("tickets").stream()
    for t in tickets:
        data = t.to_dict()
        if data.get("status") == "todo" and data.get("id") is None and data.get("archived") is None:
            print(f"Borrando ticket fantasma (IA antigua) en {p}: {t.id} - {data.get('title')}")
            t.reference.delete()
            deleted_count += 1

print(f"Limpieza completada. {deleted_count} tickets fantasma borrados.")
