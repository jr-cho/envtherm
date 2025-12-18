import pandas as pd

from src.envelope import EnvelopeElement
from src.thermal_model import DataCenterThermalModel
from src.io import load_materials

# Thermal Conditions
T_INSIDE = 22.0      # °C
T_OUTSIDE = 35.0     # °C
INTERNAL_LOAD = 5000 # W

# Building Geometry
LENGTH = 10.0  # m
WIDTH  = 5.0   # m
HEIGHT = 3.0   # m

WALL_AREA_TOTAL = 2 * (LENGTH * HEIGHT) + 2 * (WIDTH * HEIGHT)
ROOF_AREA = LENGTH * WIDTH

# Load Materials
materials = load_materials("data/materials.csv")

results = []

for name, material in materials.items():
    walls = EnvelopeElement(
        name="Walls",
        area=WALL_AREA_TOTAL,
        materials=[material]
    )

    roof = EnvelopeElement(
        name="Roof",
        area=ROOF_AREA,
        materials=[material]
    )

    model = DataCenterThermalModel(
        envelope_elements=[walls, roof],
        internal_load=INTERNAL_LOAD
    )

    cooling = model.cooling_load(T_INSIDE, T_OUTSIDE)

    results.append({
        "material": name,
        "wall_area_m2": WALL_AREA_TOTAL,
        "roof_area_m2": ROOF_AREA,
        "cooling_load_W": cooling,
        "cooling_load_kW": cooling / 1000,
        "R_value_m2K_W": material.r_value
    })

df = pd.DataFrame(results).sort_values("cooling_load_W")

print(df)
df.to_csv("results/baseline_results.csv", index=False)
