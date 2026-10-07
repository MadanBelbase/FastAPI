from fastapi import  FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import List, Dict, Annotated, Optional, Literal
from schema.user_input import UserInput
from schema.prediction_schema import PredictionResponse
from  model.predict import predict_output  , model,MODEL_VERSION




app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

#machine
@app.get('/health')
def health_check():
    return {"status": "healthy", 
    "model_version": MODEL_VERSION,
    "model_loaded": True if model else False}


@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input  = {  
            "age": data.age,
           'age_group': data.age_group,
           'lifestyle_risk': data.lifestyle_risk,
           'city_tier': data.city_tier,
           'income_lpa': data.income_lpa,
           'occupation': data.occupation,
    }
    try: 
         prediction = predict_output(user_input)
         return JSONResponse(status_code=200, content={'response':prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
