import argparse
from reporting import generate_report

from analysis import (
    load_data,
    calculate_statistics,
    calculate_regression,
    calculate_residuals,
    evaluate_model,
    validate_data
)

from visualization import (
    plot_regression,
    plot_residuals
)

def main():
    # Load experimental data
    parser = argparse.ArgumentParser(
        description="Scientific Data Analyzer"
    )

    parser.add_argument(
        "filepath",
        nargs="?",
        default="data/experimental_data.csv",
        help="Path to experimental CSV file"
    )

    args = parser.parse_args()

    try:
        df = load_data(args.filepath)

        validate_data(df)

    except FileNotFoundError:
        print(f"Error: File not found: {args.filepath}")
        return

    except ValueError as error:
        print(f"Invalid dataset: {error}")
        return

    x = df["Day"].to_numpy()
    y = df["Measurement"].to_numpy()

    # Perform scientific analysis
    stats = calculate_statistics(df)

    slope, intercept, y_pred = calculate_regression(x, y)

    residuals = calculate_residuals(y, y_pred)

    metrics = evaluate_model(y, y_pred)

    # Display results
    print("SCIENTIFIC DATA ANALYZER")
    print("------------------------")

    print("\nDescriptive Statistics:")

    for name, value in stats.items():
        print(f"{name}: {value:.4f}")

    print("\nRegression Parameters:")
    print(f"Slope: {slope:.4f}")
    print(f"Intercept: {intercept:.4f}")

    print("\nModel Performance:")

    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")

    # Generate figues
    plot_regression(x, y, y_pred)
    plot_residuals(x, residuals)

    # Generate Scientific report
    generate_report(stats, slope, intercept, metrics)

    print("\nAnalysis complete.")
    print("Figures saved to results folder.")

if __name__ == "__main__":
    main()