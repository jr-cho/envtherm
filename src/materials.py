class Material:
    def __init__(self, name, conductivity, thickness):
        self.name = name
        self.k = conductivity              # W/m*K
        self.L = thickness                 # m

    @property
    def r_value(self):
        return self.L / self.k
    
    def __repr__(self):
        return f"{self.name} (R={self.r_value:.3f} m^2K/W)"