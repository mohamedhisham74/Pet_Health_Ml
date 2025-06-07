import pandas as pd
from src.request import Pet  # Use absolute import
from src.config import DISEASE_DESCRIPTIONS

def predict_new(data: Pet, model):
    # Convert the Pydantic model to a DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Make predictions
    y_pred = model.predict(df)
    predicted_class = y_pred[0]
    disease_info = DISEASE_DESCRIPTIONS.get(predicted_class, {
        "label": "Unknown",
        "description": "No description available.",
        "treatment": "N/A",
        "severity": "Unknown",
        "recommendation": "Please consult a veterinarian."
    })
    y_prob = model.predict_proba(df)
    
    return {
        "prediction": predicted_class,
        #"probability": float(y_prob[0])
    }