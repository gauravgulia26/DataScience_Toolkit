# main.py
import warnings
from src.config import DATA_PATH
from src.data_preprocessing import preprocess_data
from src.feature_engineering import feature_engineering
from src.model_training import train_models
from src.evaluation import evaluate_models
warnings.filterwarnings('ignore')


def main():
    # Step 1: Load and preprocess data
    df = preprocess_data(DATA_PATH)

    # Step 2: Feature Engineering
    data, transformer = feature_engineering(df)

    # Step 3: Split data into features and target
    X = data[:, :-1]
    y = data[:, -1].astype("int")

    # Step 4: Train models
    models = train_models(X, y)

    # Step 5: Evaluate models
    results = evaluate_models(models, X, y)
    for model_name, metrics in results.items():
        print(f"Model: {model_name}")
        print(f"Accuracy: {metrics['Accuracy']}")
        print(f"Cross-Validation Mean Accuracy: {metrics['Cross-Validation Mean Accuracy']}")
        print("Classification Report:")
        print(metrics["Classification Report"])
        print("-" * 50)


if __name__ == "__main__":
    main()
