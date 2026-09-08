import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()
cred = credentials.Certificate("./firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

projects = ["data-ia", "timecare", "ticketingapp-2e4f1"] # A few guesses, or we can iterate over all projects
docs = db.collection("projects").stream()
for p in docs:
    tickets = db.collection("projects").document(p.id).collection("tickets").stream()
    for t in tickets:
        data = t.to_dict()
        if not data: continue
        
        # Check if createdAt is a string
        created_at = data.get("createdAt")
        updated_at = data.get("updatedAt")
        
        needs_fix = False
        if isinstance(created_at, str):
            needs_fix = True
        if isinstance(updated_at, str):
            needs_fix = True
            
        if needs_fix:
            print(f"Borrando ticket corrupto {t.id} en proyecto {p.id} (tiene fechas como string)")
            t.reference.delete()

print("Limpieza completada.")
