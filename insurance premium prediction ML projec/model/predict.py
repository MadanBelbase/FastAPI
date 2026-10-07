import pickle 
import pandas as pd

# import the model 
with open ('model/model.pkl','rb') as file:
    model = pickle.load(file)

MODEL_VERSION =' 1.0.0'

#get class labels from model (important for multi-class classification)
class_labels =  model.classes_.tolist()

def predict_output(uesr_input: dict):
    df = pd.DataFrame([uesr_input])

    #predict the class
    predicted_class = model.predict(df)[0]

    probabilities =model.predict(df)[0]
    confidance = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambada p:  round(p, 4), probabilities)))

    return {
        "predicte_catogery ": predicted_class,
        "confidance": confidance,
        "class_probabilities": class_probs,
    }

