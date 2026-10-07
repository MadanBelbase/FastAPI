from pydantic import BaseModel,Field
from typing import dict

class PredictionResponse(BaseModel):
    predicted_category :str = Field(..., description="The prediction insurance premium ",
    example="High")
    confidance : float = Field(..., description="The confidence score of the prediction",
    example=0.85)

    class_probabilities : dict = Field(..., description="The probabilities of each class",
    example={"Low": 0.1, "Medium": 0.05, "High": 0.85})
    