# Ethiopia Financial Inclusion Forecasting System

## Business Objective
Selam Analytics has been engaged by a consortium of stakeholders (National Bank of Ethiopia, mobile money operators, and DFIs) to build a forecasting system that tracks and predicts Ethiopia's digital financial transformation. The goal is to understand the drivers of financial inclusion and predict progress for 2026 and 2027 based on historical observations and key market events.

## Project Structure
```text
ethiopia-fi-forecast/
├── .github/workflows/          # CI/CD pipelines
│   └── unittests.yml
├── data/
│   ├── raw/                    # Original Excel starter datasets
│   └── processed/              # Enriched and cleaned CSV data
├── notebooks/                  # Analysis logic
│   ├── 01_data_exploration_and_enrichment.ipynb
│   └── 02_exploratory_data_analysis.ipynb
├── reports/                    # Key Findings
│   └── eda_insights.md         # Summary of 5 key insights from Task 2
├── data_enrichment_log.md      # Detailed log of added data points (Task 1)
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

### Task 1: Data Enrichment

The primary dataset has been enriched with 2024 Findex data and recent infrastructure milestones. All changes are documented in `data_enrichment_log.md`.

### Task 2: Exploratory Data Analysis

Analyzed the "Access-Usage Paradox" where mobile money adoption is outpacing traditional account growth. Findings on gender gaps and event-driven spikes are documented in `reports/eda_insights.md`.
