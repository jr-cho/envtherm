class EnvelopeElement:
    def __init__(self, name, area, materials):
        self.name = name
        self.area = area
        self.materials = materials

    @property
    def total_r(self):
        return sum(m.r_value for m in self.materials)
    
    def heat_transfer(self, t_inside, t_outside):
        """
            This function will return heat transfer rate (W)   |   Positive value = heat entering the space
        """

        return self.area * (t_outside - t_inside) / self.total_r