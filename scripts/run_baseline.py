import pandas as pd
import numpy as np

from src.envelope import EnvelopeElement
from src.thermal_model import DataCenterThermalModel
from src.io import load_materials

# Simulation Parameters
T_INSIDE = 22.0      # C
T_OUTSIDE = 35.0     # C
INTERNAL_LOAD = 5000 # W
WALL_AREA = 50.0     # m^2

# Load Materials
materials = load_materials("data/materials.csv")

results = []

for name, material in materials.items():
    wall = EnvelopeElement(
        name="Wall",
        area=WALL_AREA,
        materials=[material]
    )

    model = DataCenterThermalModel(
        envelope_elements=[wall],
        internal_load=INTERNAL_LOAD
    )

    cooling = model.cooling_load(T_INSIDE, T_OUTSIDE)

    results.append({
        "material": name,
        "cooling_load_W": cooling,
        "cooling_load_kW": cooling / 1000,
        "R_value_m2K_W": material.r_value
    })

# Results Data bFrame
df = pd.DataFrame(results)
df = df.sort_values("cooling_load_W")

print(df)

# Save for plots / docs
df.to_csv("results/baseline_results.csv", index=False)