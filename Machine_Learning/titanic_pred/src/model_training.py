# src/model_training.py

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def train_models(X, y):
    pipelines = {
        "Random Forest": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
            ]
        ),
        "Logistic Regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
            ]
        ),
        "Decision Tree": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", DecisionTreeClassifier(random_state=42)),
            ]
        ),
        "Naive Bayes": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", GaussianNB()),
            ]
        ),
    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    models = {}
    for model_name, pipeline in pipelines.items():
        pipeline.fit(X_train, y_train)
        models[model_name] = {"model": pipeline, "X_test": X_test, "y_test": y_test}
    return models
