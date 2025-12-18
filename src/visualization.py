import matplotlib.pyplot as plt

def plot_results(material_names, cooling_loads):
    plt.figure()
    plt.bar(material_names, cooling_loads)
    plt.ylabel("Cooling Load (W)")
    plt.xlabel("Envelope Material")
    plt.title("Cooling Load by Envelope Material")
    plt.tight_layout()
    plt.show()