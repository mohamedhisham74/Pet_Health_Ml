import os
import joblib 

from dotenv import load_dotenv

DISEASE_DESCRIPTIONS = {
    "Rabies": {
        "label": "Rabies",
        "description": "A viral disease that affects the central nervous system and is almost always fatal once symptoms appear.",
        "treatment": "There is no effective treatment once symptoms appear. Euthanasia is often recommended for infected animals.",
        "severity": "Very High",
        "recommendation": "Immediate quarantine and notify health authorities. Vaccination is essential for prevention."
    },
    "Ringworm": {
        "label": "Ringworm",
        "description": "A fungal skin infection that causes circular patches of hair loss and scaly skin.",
        "treatment": "Topical antifungal creams, medicated shampoos, and in severe cases, oral antifungal medications.",
        "severity": "Low to Moderate",
        "recommendation": "Maintain good hygiene, isolate infected animals, and disinfect the environment."
    },
    "Ear Infection": {
        "label": "Ear Infection",
        "description": "An infection of the external, middle, or inner ear, common in pets with floppy ears or allergies.",
        "treatment": "Ear cleaning, antibiotics or antifungal medications depending on the cause.",
        "severity": "Moderate",
        "recommendation": "Clean the ears regularly and follow up with a vet for proper diagnosis and medication."
    },
    "Obesity": {
        "label": "Obesity",
        "description": "Excess body fat that can lead to various health problems such as joint pain, diabetes, and heart issues.",
        "treatment": "Controlled diet, increased physical activity, and regular weight monitoring.",
        "severity": "Moderate",
        "recommendation": "Adjust feeding practices, encourage exercise, and consult a vet for a weight loss plan."
    }
}

#load .env 

load_dotenv(override=True)

APP_NAME=os.getenv("PET_Health-API")
VERSION=os.getenv("VERSION")
SECRET_KEY_TOKEN="44f5a4dlf2c7d717ad1601cdaf47a3c030afD88c"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_FOLDER_PATH = os.path.join(BASE_DIR, "artifacts")


#load Model 
model = joblib.load(os.path.join(ARTIFACTS_FOLDER_PATH, 'model.pkl'))