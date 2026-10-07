import pickle
import pandas as pd

# Import the model
with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

MODEL_VERSION = "1.0.0"

# Get class labels from model (important for multi-class classification)
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for each class
    probabilities = model.predict_proba(df)[0]

    # Get confidence of the predicted class
    confidence = max(probabilities)

    # Map class labels to their probabilities
    class_probs = dict(
        zip(
            class_labels,
            map(lambda p: round(p, 4), probabilities)
        )
    )

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probs,
    }
