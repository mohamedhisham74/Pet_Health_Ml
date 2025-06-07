from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from src.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, model
from src.inference import predict_new
from src.request import Pet

# Initialize FastAPI app
app = FastAPI(title=APP_NAME or "PET_Health-API", version=VERSION or "1.0")

# API Key Security
api_key_header = APIKeyHeader(name="X-API-key")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid API Key")
    return api_key

@app.get("/", tags=["Health Check"], description="API Health Check")
async def home(api_key: str = Depends(verify_api_key)):
    return {
        "message": f"Welcome to {APP_NAME} API v{VERSION}"
    }

@app.post("/predict/horse_health", tags=["Models"], description="Predict Horse Health Outcome")
def predict_horse_health(data: Pet, api_key: str = Depends(verify_api_key)):
    try:
        result = predict_new(data=data,  model=model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
