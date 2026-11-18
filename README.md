# Scientific Data Analyzer

A Python Application for analyzing experimental data using descriptive statistics, linear regression, and model evaluation.

## Features

- Import experimental data from CSV files
- Calculate descriptive statistics
- Perform linear regression
- Calculate residuals
- Evaluate models using SSE, MSE, RMSE, MAE, and R<sup>2</sup>
- Validate input datasets
- Generate regression and residual plots
- Export a text analysis report
- Run automated tests with pytest

## Technologies

Python, NumPy, pandas, SciPy, Matplotlib, pytest

## Installation

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Usage

Run the analyzer with the default dataset:
```bash
python main.py
```

Analyze another compatible CSV file:
```bash
python main.py data/experimental_data.csv
```

Input files must contain numeric 'Day' and 'Measurement' columns.

## Testing
```bash
python -m pytest -v
```

## Project Structures

- `main.py` - application entry point
- `analysis.py` - statistics, regression, validation, and metrics
- `visualization.py` - plot generation
- `reporting.py` - report generation
- `tests/` - automated tests
- `data/` - sample experimental data
- `results/` - generated reports and figures

## Development & Learning

This project was developed as part of my self-directed learning in Python, scientific computing, and software engineering.
I used Chat GPT as an AI assisted tutor to help structure lessons, explain programming concepts, troubleshoot errors, and introduce software development best practices.
Throughout development, I practiced implementing and testing Python functions, analyzing experimental data, interpreting regression results, and organizing code into reusable modules.
The goal of this project was not only to build a functional scientific analysis application but also to strengthen my understanding of Python programming ans develop practical software engineering skills.