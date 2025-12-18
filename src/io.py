import pandas as pd
from src.materials import Material

def load_materials(csv_path):
    df = pd.read_csv(csv_path)
    materials = {}

    for _, row in df.iterrows():
        materials[row["name"]] = Material(
            name=row["name"],
            conductivity=row["conductivity_W_mK"],
            thickness=row["thickness_m"]
        )

    return materials