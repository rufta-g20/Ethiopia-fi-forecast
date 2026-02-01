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
│   └── processed/              # Enriched and cleaned CSV data for modeling
├── notebooks/                  # Data exploration and enrichment logic
│   └── 01_data_exploration_and_enrichment.ipynb
├── src/                        # Source code for data processing
├── dashboard/                  # Streamlit visualization app
├── tests/                      # Unit tests
├── models/                     # Saved forecasting models
├── reports/                    # Analysis figures and documentation
├── data_enrichment_log.md      # Detailed log of added data points
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

2. **Create the Environment:**
```bash
conda create -n kaim_week10 python=3.11 -y
conda activate kaim_week10

```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```

### Data Enrichment (Task 1)

The primary dataset has been enriched with 2024 Findex data and recent infrastructure milestones. All changes are documented in `data_enrichment_log.md`.