from pydantic import BaseModel, Field
from typing import Literal

class Pet(BaseModel):
    # Categorical features with restricted literal values:
    pet_type: str = Field(..., description="Type of pet (e.g., horse, dog, cat).")
    breed_category: str = Field(..., description="Breed category of the pet.")
    vaccination_status: str = Field(..., description="Vaccination status of the pet.")
    
    # Numerical features:
    age: int = Field(..., description="Age of the horse in years.")
    weight: float = Field(..., description="Weight of the horse in kilograms.")
    temperature: float = Field(..., description="Body temperature of the horse.")
    heart_rate: int = Field(..., description="Heart rate (pulse) of the horse.")
    activity_level: int = Field(..., description="Activity level on a scale.")
    eating_habits: int = Field(..., description="Eating habits represented numerically.")
    hydration: float = Field(..., description="Hydration level of the horse.")
    exercise_hours: float = Field(..., description="Number of hours the horse exercises per day.")
    sick: int = Field(..., description="Indicates if the horse is sick (1 for yes, 0 for no).")
