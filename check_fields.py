import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()
cred = credentials.Certificate("./firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

sprinto_ticket = db.collection("projects").document("timecare").collection("tickets").document("to9RE5kDcg12JCzOOjVR").get()
print("--- TICKET NORMAL CREADO EN SPRINTO ---")
print(sprinto_ticket.to_dict())

epic_ticket = db.collection("projects").document("timecare").collection("tickets").document("xpl8AIXdwJrXqKCI8M6a").get()
print("\n--- EPICA CREADA EN SPRINTO ---")
print(epic_ticket.to_dict())
