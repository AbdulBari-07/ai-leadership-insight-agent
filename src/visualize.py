import matplotlib.pyplot as plt

def plot_revenue(data):
    quarters = list(data.keys())
    values = list(data.values())

    plt.figure()
    plt.plot(quarters, values)
    plt.xlabel("Quarter")
    plt.ylabel("Revanue")
    plt.title("Revenu Trend")
    plt.savefig("outputs/plots/revenue.png")
    plt.close()