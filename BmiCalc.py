from fastapi import FastAPI


app = FastAPI()

@app.get("/")

def Hi():
    return {"message": "Sup Fasty"}

@app.get("/calculate_bmi")
def calculate_bmi(weight: float, height: float):
    bmi = weight / (height ** 2)
    
    
    if bmi < 18.5:
        message = "You're underweight, eat more."
    elif 18.5 <= bmi < 25:
        message = "You're all good, keep it that way."
    elif 25 <= bmi < 30:
        message = "You're overweight, excercise more."
    else:
        message = "You're too fat, go see a doctor."

    return {
            "bmi": bmi,
            "message": message
    }
