# src/feature_engineering.py

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import PowerTransformer


def feature_engineering(df):
    kn = KNNImputer(weights="distance", n_neighbors=5)
    pt = PowerTransformer(standardize=False)
    sc = SimpleImputer(strategy="most_frequent")
    sc_constant = SimpleImputer(strategy="constant", fill_value=0)

    transformer = ColumnTransformer(
        transformers=[
            ("knn_impute", kn, ["Room_number"]),
            ("mode_imputation", sc, ["Embarked", "Cabin_number"]),
            ("constant_imputation", sc_constant, ["Room_number"]),
            ("power_transform", pt, ["Fare"]),
        ],
        remainder="passthrough",
    )

    pipe = Pipeline(steps=[("trf", transformer)])
    data = pipe.fit_transform(df)
    return data, pipe
