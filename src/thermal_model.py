class DataCenterThermalModel:
    def __init__(self, envelope_elements, internal_load):
        self.envelope_elements = envelope_elements
        self.internal_load = internal_load

    def envelope_heat_gain(self, t_inside, t_outside):
        return sum(
            e.heat_transfer(t_inside, t_outside)
            for e in self.envelope_elements
        )
    
    # Formula: Q_cooling = Q_internal + Q_envelope
    def cooling_load(self, t_inside, t_outside):
        # Cooling required to maintain the indoor set point (W)
        q_env = self.envelope_heat_gain(t_inside, t_outside)
        return self.internal_load + q_env