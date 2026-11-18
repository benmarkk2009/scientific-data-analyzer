import matplotlib.pyplot as plt
from pathlib import Path

def plot_regression(x, y, y_pred):

    Path("results").mkdir(exist_ok=True)

    plt.figure(figsize=(9, 5))

    plt.scatter(x, y, label="Experimental Data")
    plt.plot(x, y_pred, color="red", label="Linear Fit")

    plt.xlabel("Day")
    plt.ylabel("Measurement")
    plt.title("Linear Regression Analysis")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/linear_regression.png", dpi=300,
                bbox_inches="tight")
    plt.close()

def plot_residuals(x, residuals):

    Path("results").mkdir(exist_ok=True)

    plt.figure(figsize=(9, 5))

    plt.scatter(x, residuals)
    plt.axhline(0, color="red", linestyle="--")

    plt.xlabel("Day")
    plt.ylabel("Residual")
    plt.title("Residual Analysis")
    plt.grid(True)

    plt.savefig("results/residual_plot.png",
                dpi=300, bbox_inches="tight")
    
    plt.close()