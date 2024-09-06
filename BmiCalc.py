from fastapi import FastAPI, Query
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class BMIOutput(BaseModel):
    bmi: float
    message: str




@app.get("/")

def Hi():
    return {"message": "Sup Fasty"}

@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float = Query(..., gt= 20, lt=200, description="weight (kg)"),
    height: float = Query(..., gt= 1, lt=3, description="height (m)")):
    bmi = weight / (height ** 2)
    
    
    if bmi < 18.5:
        message = "You're underweight, eat more."
    elif 18.5 <= bmi < 25:
        message = "You're all good, keep it that way."
    elif 25 <= bmi < 30:
        message = "You're overweight, excercise more."
    else:
        message = "You're too fat, go see a doctor."

    return BMIOutput(bmi=bmi,message=message)
