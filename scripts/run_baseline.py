from src.materials import Material
from src.envelope import EnvelopeElement
from src.thermal_model import DataCenterThermalModel

# Temperatures (°C)
T_INSIDE = 22.0
T_OUTSIDE = 35.0

# Internal heat load (W)
INTERNAL_LOAD = 5000

# Define materials
concrete = Material("Concrete", 1.7, 0.20)

# Define envelope
wall = EnvelopeElement(
    name="Wall",
    area=50.0,
    materials=[concrete]
)

# Build model
model = DataCenterThermalModel(
    envelope_elements=[wall],
    internal_load=INTERNAL_LOAD
)

cooling = model.cooling_load(T_INSIDE, T_OUTSIDE)
print(f"Cooling load: {cooling/1000:.2f} kW")