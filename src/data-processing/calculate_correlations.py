from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
PROCESSED_DIR = BASE_DIR / "processed"
INPUT_PATH = PROCESSED_DIR / "country_data.csv"
OUTPUT_PATH = PROCESSED_DIR / "correlation_results.csv"
LATEX_OUTPUT_PATH = PROCESSED_DIR / "correlation_results_latex.txt"

HYPOTHESES = [
    {
        "hypothesis": "H1",
        "description": "Housing Price Index and Mortgage Rate",
        "x": "housing_price_index",
        "y": "mortgage_rate",
    },
    {
        "hypothesis": "H2",
        "description": "Housing Price Index and Income",
        "x": "housing_price_index",
        "y": "income",
    },
    {
        "hypothesis": "H3",
        "description": "Housing Price Index and Unemployment",
        "x": "housing_price_index",
        "y": "unemployment",
    },
]


def classify_correlation(value: float) -> str:
    absolute_value = abs(value)

    if absolute_value < 0.20:
        return "very weak"
    if absolute_value < 0.40:
        return "weak"
    if absolute_value < 0.60:
        return "moderate"
    if absolute_value < 0.80:
        return "strong"
    return "very strong"


def calculate_pearson(df: pd.DataFrame, x_column: str, y_column: str):
    subset = df[["country", "year", x_column, y_column]].copy()
    subset[x_column] = pd.to_numeric(subset[x_column], errors="coerce")
    subset[y_column] = pd.to_numeric(subset[y_column], errors="coerce")
    subset = subset.dropna(subset=[x_column, y_column])

    if len(subset) < 2:
        return None, len(subset)

    correlation = subset[x_column].corr(subset[y_column], method="pearson")
    return correlation, len(subset)


def main():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)

    required_columns = {
        "country",
        "year",
        "housing_price_index",
        "mortgage_rate",
        "income",
        "unemployment",
    }

    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df = df[(df["year"] >= 2005) & (df["year"] <= 2023)]

    results = []

    for item in HYPOTHESES:
        correlation, observations = calculate_pearson(df, item["x"], item["y"])

        if correlation is None or pd.isna(correlation):
            rounded = None
            strength = "not available"
        else:
            rounded = round(float(correlation), 2)
            strength = classify_correlation(float(correlation))

        results.append(
            {
                "hypothesis": item["hypothesis"],
                "relationship": item["description"],
                "x_variable": item["x"],
                "y_variable": item["y"],
                "pearson_correlation": rounded,
                "strength": strength,
                "observations": observations,
            }
        )

    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_PATH, index=False)

    print("\nPearson correlation results:")
    print(results_df.to_string(index=False))
    print(f"\nSaved CSV results to: {OUTPUT_PATH}")

    latex_lines = [
        "\\begin{table}[H]",
        "    \\centering",
        "    \\begin{tabular}{l l r r}",
        "        \\toprule",
        "        \\textbf{Hypothesis} & \\textbf{Relationship} & \\textbf{Pearson coefficient} & \\textbf{Observations} \\\\",
        "        \\midrule",
    ]

    for row in results:
        latex_lines.append(
            f"        {row['hypothesis']} & {row['relationship']} & "
            f"{row['pearson_correlation']} & {row['observations']} \\\\"
        )

    latex_lines.extend(
        [
            "        \\bottomrule",
            "    \\end{tabular}",
            "    \\caption{Pearson correlation coefficients for the selected housing affordability indicators.}",
            "    \\label{tab:pearson_correlations}",
            "\\end{table}",
        ]
    )

    LATEX_OUTPUT_PATH.write_text("\n".join(latex_lines), encoding="utf-8")
    print(f"Saved LaTeX table to: {LATEX_OUTPUT_PATH}")


if __name__ == "__main__":
    main()