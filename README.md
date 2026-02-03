# Ethiopia Financial Inclusion Forecasting System

## Business Objective
Selam Analytics has been engaged by a consortium of stakeholders (National Bank of Ethiopia, mobile money operators, and DFIs) to build a forecasting system that tracks and predicts Ethiopia's digital financial transformation. The goal is to understand the drivers of financial inclusion and predict progress for 2026 and 2027 based on historical observations and key market events.

## Project Structure
```text
ethiopia-fi-forecast/
├── .github/workflows/          # CI/CD pipelines
│   └── unittests.yml
├── dashboard/
│   └── app.py                  # Task 5: Streamlit Dashboard Application
├── data/
│   ├── raw/                    # Original Excel starter datasets
│   └── processed/              # Enriched CSV data (ethiopia_fi_enriched.csv)
├── notebooks/                  # Analysis logic
│   ├── 01_data_exploration_and_enrichment.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_event_impact_modeling.ipynb  # Task 3: Impact Matrix logic
│   └── 04_forecasting_access_usage.ipynb  # Task 4: Prophet Models
├── reports/                   
│   ├── eda_insights.md         # Task 2: Summary of 5 key insights
│   ├── impact_methodology.md   # Task 3: Association Matrix & Validation
│   └── forecast_interpretation.md # Task 4 interpretation
├── data_enrichment_log.md      # Task 1: Detailed log of added data points
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview
```

## Getting Started

### Prerequisites

* Python 3.11
* Conda (Miniconda or Anaconda)

### Installation & Setup

1. **Clone the repository:**
```bash
git clone git@github.com:rufta-g20/ethiopia-fi-forecast.git
cd ethiopia-fi-forecast

```

2. **Setup Environment:**
```bash
conda create -n kaim_week10 python=3.11 -y
conda activate kaim_week10
pip install -r requirements.txt

```

## Progress Summary

### Task 1: Data Enrichment

The primary dataset has been enriched with 2024 Findex data and recent infrastructure milestones. All changes are documented in `data_enrichment_log.md`.

### Task 2: Exploratory Data Analysis

Analyzed the "Access-Usage Paradox" where mobile money adoption is outpacing traditional account growth. Findings on gender gaps and event-driven spikes are documented in `reports/eda_insights.md`.

### Task 3: Event Impact Modeling

Developed an Association Matrix to quantify how events like the Telebirr launch and Fayda ID rollout drive indicators. Validated the model against 2021-2024 data, establishing a 1.58pp growth scaler per impact point. Findings are documented in `reports/impact_methodology.md`.

### Task 4: Forecasting Access and Usage

Deployed Event-Augmented Prophet models to forecast inclusion through 2027. Established baseline, optimistic, and pessimistic scenarios, projecting a range of 62.3% to 66.2% for account ownership by end-of-2027. Documented in `reports/forecast_interpretation.md`.

### Task 5: Dashboard Development

Created an interactive Streamlit dashboard allowing stakeholders to visualize trends, event impacts, and toggle between inclusion scenarios.

### Running the Dashboard Locally

Navigate to the project root and run:
```bash
streamlit run dashboard/app.py
```