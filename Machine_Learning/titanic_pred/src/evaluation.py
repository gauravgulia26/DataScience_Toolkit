# src/evaluation.py

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
import numpy as np


def evaluate_models(models, X, y):
    results = {}
    for model_name, data in models.items():
        pipeline = data["model"]
        y_pred = pipeline.predict(data["X_test"])
        accuracy = accuracy_score(data["y_test"], y_pred)
        cv_scores = cross_val_score(pipeline, X, y, cv=5)
        results[model_name] = {
            "Accuracy": accuracy,
            "Cross-Validation Mean Accuracy": np.mean(cv_scores),
            "Classification Report": classification_report(data["y_test"], y_pred),
        }
    return results
