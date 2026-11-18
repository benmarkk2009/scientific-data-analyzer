from pathlib import Path

def generate_report(stats, slope, intercept,metrics):
    """Generate a scientific analysis report."""

    Path("results").mkdir(exist_ok=True)

    with open("results/analysis_report.txt", "w",
                encoding="utf-8") as file:
        
        file.write("Scientific Data Analyzer\n")
        file.write("========================\n")

        file.write("\nDescriptive Statistics:\n")

        for name, value in stats.items():
            file.write(f"{name}: {value:.4f}\n")
        
        file.write("\nRegression Parameters:\n")

        file.write(f"Slope: {slope:.4f}\n")
        file.write(f"Intercept: {intercept:.4f}\n")
        file.write(f"Regression Equation: y = {slope:.4f}x + {intercept:.4f}\n")
        file.write("\nModel Performance:\n")

        for name, value in metrics.items():
            file.write(f"{name}: {value:.4f}\n")
    print("Report saved successfully.")