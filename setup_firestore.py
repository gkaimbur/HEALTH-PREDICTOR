#!/usr/bin/env python3
"""
Setup Firestore database collections and seed initial data
"""

import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path
import json
from datetime import datetime, timedelta
import random

# Load Firebase credentials
cred_path = Path('firebase-service-account.json')
if not cred_path.exists():
    print("❌ ERROR: firebase-service-account.json not found!")
    exit(1)

print(f"📋 Loading credentials from {cred_path}...")
cred = credentials.Certificate(str(cred_path))

# Initialize Firebase
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
print("✅ Connected to Firebase Firestore")

# Create demo patients if collection is empty
print("\n📝 Seeding demo patients...")

try:
    existing_docs = list(db.collection('patients').limit(1).stream())
    if existing_docs:
        print("✓ Patients collection already has data. Skipping seeding.")
    else:
        demo_patients = [
            {
                'id': 'patient_001',
                'name': 'Alice Johnson',
                'dob': '1990-03-15',
                'visits': [
                    {
                        'label': 'Visit 1 (Week 12)',
                        'date': (datetime.now() - timedelta(days=30)).isoformat(),
                        'sbp': 128,
                        'dbp': 82,
                        'bmi': 24.5,
                        'blood_sugar': 95,
                        'risk': 0.15,
                        'notes': 'Routine checkup'
                    },
                    {
                        'label': 'Visit 2 (Week 16)',
                        'date': (datetime.now() - timedelta(days=15)).isoformat(),
                        'sbp': 132,
                        'dbp': 85,
                        'bmi': 24.6,
                        'blood_sugar': 98,
                        'risk': 0.22,
                        'notes': 'Mild elevation in BP'
                    }
                ]
            },
            {
                'id': 'patient_002',
                'name': 'Sarah Mitchell',
                'dob': '1988-07-22',
                'visits': [
                    {
                        'label': 'Visit 1 (Week 20)',
                        'date': (datetime.now() - timedelta(days=45)).isoformat(),
                        'sbp': 145,
                        'dbp': 95,
                        'bmi': 28.2,
                        'blood_sugar': 115,
                        'risk': 0.68,
                        'notes': 'High BP readings'
                    },
                    {
                        'label': 'Visit 2 (Week 24)',
                        'date': (datetime.now() - timedelta(days=20)).isoformat(),
                        'sbp': 148,
                        'dbp': 98,
                        'bmi': 28.3,
                        'blood_sugar': 118,
                        'risk': 0.75,
                        'notes': 'Continued monitoring'
                    },
                    {
                        'label': 'Visit 3 (Week 28)',
                        'date': (datetime.now() - timedelta(days=5)).isoformat(),
                        'sbp': 150,
                        'dbp': 100,
                        'bmi': 28.4,
                        'blood_sugar': 120,
                        'risk': 0.82,
                        'notes': 'Close monitoring recommended'
                    }
                ]
            },
            {
                'id': 'patient_003',
                'name': 'Emma Rodriguez',
                'dob': '1992-11-08',
                'visits': [
                    {
                        'label': 'Visit 1 (Week 8)',
                        'date': (datetime.now() - timedelta(days=60)).isoformat(),
                        'sbp': 118,
                        'dbp': 76,
                        'bmi': 22.1,
                        'blood_sugar': 88,
                        'risk': 0.05,
                        'notes': 'Normal baseline'
                    }
                ]
            },
            {
                'id': 'patient_004',
                'name': 'Jennifer Lee',
                'dob': '1989-05-19',
                'visits': [
                    {
                        'label': 'Visit 1 (Week 14)',
                        'date': (datetime.now() - timedelta(days=35)).isoformat(),
                        'sbp': 140,
                        'dbp': 90,
                        'bmi': 26.8,
                        'blood_sugar': 112,
                        'risk': 0.55,
                        'notes': 'Elevated readings'
                    }
                ]
            },
            {
                'id': 'patient_005',
                'name': 'Rebecca Davis',
                'dob': '1991-09-27',
                'visits': [
                    {
                        'label': 'Visit 1 (Week 10)',
                        'date': (datetime.now() - timedelta(days=50)).isoformat(),
                        'sbp': 125,
                        'dbp': 80,
                        'bmi': 23.5,
                        'blood_sugar': 92,
                        'risk': 0.12,
                        'notes': 'Good control'
                    },
                    {
                        'label': 'Visit 2 (Week 18)',
                        'date': (datetime.now() - timedelta(days=25)).isoformat(),
                        'sbp': 130,
                        'dbp': 84,
                        'bmi': 23.6,
                        'blood_sugar': 94,
                        'risk': 0.18,
                        'notes': 'Slight increase'
                    }
                ]
            },
        ]
        
        total_visits = 0
        for patient in demo_patients:
            patient_id = patient['id']
            patient_visits = patient.pop('visits', [])
            total_visits += len(patient_visits)
            
            # Create patient document
            db.collection('patients').document(patient_id).set({
                'name': patient['name'],
                'dob': patient['dob'],
                'updated_at': firestore.SERVER_TIMESTAMP
            })
            print(f"  ✓ Created patient: {patient['name']} ({patient_id})")
            
            # Create visits subcollection
            for visit in patient_visits:
                visit_label = visit['label']
                db.collection('patients').document(patient_id).collection('visits').document(visit_label).set(visit)
            print(f"    → Added {len(patient_visits)} visit(s)")
        
        print(f"\n✅ Seeded {len(demo_patients)} demo patients with {total_visits} total visits")

except Exception as e:
    print(f"❌ Error seeding patients: {e}")
    exit(1)

print("\n" + "="*60)
print("✅ FIRESTORE SETUP COMPLETE!")
print("="*60)
print("\nYour Firestore database is ready:")
print("  📦 Collection: 'patients'")
print("  └─ Subcollections: 'visits' (per patient)")
print("\nYou can now run the Streamlit app:")
print("  $ streamlit run app.py")
print("\n")
