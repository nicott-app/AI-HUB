import sys
import os
import firebase_admin
from firebase_admin import credentials, firestore

def test_db():
    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase-credentials.json")
    if not os.path.exists(cred_path):
        print("No firebase-credentials.json found!")
        return

    try:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    except ValueError:
        pass # Already initialized

    db = firestore.client()

    projects = list(db.collection("projects").limit(5).stream())
    print(f"Projects found: {len(projects)}")
    
    for p in projects:
        print(f"Project: {p.id}")
        tickets = list(db.collection("projects").document(p.id).collection("tickets").limit(20).stream())
        print(f"  Tickets found: {len(tickets)}")
        for t in tickets:
            data = t.to_dict()
            print(f"    - [{t.id}] type: '{data.get('type')}', status: '{data.get('status')}', title: '{data.get('title')}'")

if __name__ == "__main__":
    test_db()
