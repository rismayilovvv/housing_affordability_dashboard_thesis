# Housing Affordability Dashboard

This project is a prototype web application developed for a bachelor thesis on housing affordability in selected European countries from 2005 to 2023.

The source code is available on GitHub:

https://github.com/rismayilovvv/housing_affordability_dashboard_thesis

The application allows users to explore and compare housing affordability indicators, including:

- Housing Price Index (HPI)
- Mortgage rates
- Income
- Unemployment
- GDP
- Population

The system consists of three main parts:

- **Data processing:** Python scripts for cleaning and preparing datasets
- **Backend:** FastAPI server connected to PostgreSQL
- **Frontend:** React dashboard with interactive charts and a mortgage simulator

---

## Project Structure

```text
housing-affordability-thesis/
├── src/
│   ├── backend/                 # FastAPI backend and database loading script
│   ├── data-processing/         # Python scripts and raw/processed datasets
│   └── frontend/                # React frontend application
│
├── text/
│   ├── thesis/                  # LaTeX thesis source files
│   └── thesis.pdf               # Final thesis PDF
│
├── interactive_dashboard_testing.mp4
├── README.md
└── readme.txt
```

---

## Technologies Used

### Data Processing

- Python
- pandas

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend

- JavaScript
- React
- Vite
- Chart.js
- Axios
- React Router

---

## Prerequisites

Before running the project, install:

- Python 3.10 or later
- Node.js 18 or later
- PostgreSQL
- pgAdmin 4, optional
- Git, optional

---

## 1. Data Processing

Go to the data processing folder:

```bash
cd src/data-processing
```

Install the required dependency:

```bash
pip install pandas
```

Run the data processing script:

```bash
python process_data.py
```

The script creates the processed dataset:

```text
src/data-processing/processed/country_data.csv
```

---

## 2. Correlation Calculation

To calculate Pearson correlation coefficients used in the thesis, run:

```bash
python calculate_correlations.py
```

The results are saved in:

```text
src/data-processing/processed/correlation_results.csv
src/data-processing/processed/correlation_results_latex.txt
```

---

## 3. Database Setup

Create a PostgreSQL database, for example:

```text
housing_affordability
```

You can create it using pgAdmin or PostgreSQL command line.

If a database backup is included, it can be restored using:

```bash
psql -U postgres -d housing_affordability -f src/backend/housing_affordability_backup.sql
```

---

## 4. Backend Setup

Go to the backend folder:

```bash
cd src/backend
```

Create and activate a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install all required backend dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Before running the backend, check the database connection settings and make sure they match your local PostgreSQL setup.

Load the processed dataset into the database:

```bash
python load_data.py
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Frontend Setup

Open a new terminal and go to the frontend folder:

```bash
cd src/frontend
```

Install frontend dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

The backend must be running for the frontend to load data.

---

## Main Features

The application includes the following pages and functions:

- **Home Page:** Overview of the dashboard
- **Indicator Analysis:** Country and year filtering with multi-indicator charts
- **Compare Countries:** Comparison of selected countries by indicator
- **Mortgage Simulator:** Estimation of monthly mortgage payment and payment-to-income burden
- **Export Functions:** Download charts as PNG and data as CSV

---

## API Endpoints

Main backend endpoints:

```text
GET /countries
```

Returns the list of available countries.

```text
GET /data
```

Returns country-year indicator data.

Example:

```text
GET /data?country=Czech Republic&start_year=2005&end_year=2023
```

---

## Testing

The application was manually tested as a local prototype. Testing covered:

- page navigation
- country and year filtering
- chart rendering
- country comparison
- mortgage simulator calculations
- CSV and PNG export
- backend API responses
- database loading

A testing video is included:

```text
interactive_dashboard_testing.mp4
```

---

## Data Sources

The application uses public datasets from:

- Eurostat
- World Bank
- OECD
- Statbase
- European Central Bank, where applicable

---

## Notes

This project is developed as a local academic prototype. The correlation results are exploratory and should not be interpreted as proof of causality.

---

## Future Improvements

Possible future improvements include:

- online deployment
- automated data retrieval from APIs
- additional indicators
- more advanced statistical analysis
- user-uploaded datasets
- multi-language support
