# src/data_preprocessing.py

import pandas as pd
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import PowerTransformer, OneHotEncoder


def preprocess_data(data_path):
    df = pd.read_csv(data_path)
    df.drop(columns=["PassengerId", "Name", "Ticket"], inplace=True)

    # Feature Engineering for Cabin
    df["Cabin_number"] = df["Cabin"].str.extract(r"([A-Za-z]+)")
    df["Room_number"] = df["Cabin"].str.extract(r"([0-9]+)")
    df.drop(columns="Cabin", inplace=True)

    # One-Hot Encoding
    oc = OneHotEncoder(drop="first", sparse_output=False)
    kn = KNNImputer(n_neighbors=5, weights="distance")
    sc = SimpleImputer(strategy="most_frequent")
    sc_constant = SimpleImputer(strategy="constant", fill_value=0)
    df["Age"] = kn.fit_transform(df[["Age"]])
    df[["Cabin_number"]] = sc.fit_transform(df[["Cabin_number"]])
    df[["Room_number"]] = sc_constant.fit_transform(df[["Room_number"]])

    df["Sex"] = oc.fit_transform(df[["Sex"]])
    df["Embarked"] = oc.fit_transform(df[["Embarked"]])
    df["Cabin_number"] = oc.fit_transform(df[["Cabin_number"]])

    return df
