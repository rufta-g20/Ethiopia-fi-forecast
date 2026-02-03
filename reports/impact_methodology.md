# Methodology: Event Impact Modeling
**Analyst:** Rufta

## Modeling Approach
We used an **Association Matrix** approach to quantify the relationship between catalyst market events and Global Findex financial inclusion indicators.

### 1. Functional Form: Temporal Step Function
Impact is modeled as a **delayed step function with a linear build-up phase**:
- **Lag:** Time (in months) between an event occurring and its initial effect on indicators (e.g., a 12-month lag for Fayda ID to affect bank account opening).
- **Ramp-up:** A 6-month linear interpolation from 0 to full magnitude, representing the time required for market awareness and adoption.
- **Combined Impact:** Effects are additive across multiple events, capped at a logical maximum (e.g., 100% penetration).

### 2. Magnitude Scaling & Scoring
Qualitative assessments were converted into a numeric **Impact Score**:
- **High (3.0):** Significant structural shifts (Telebirr, National ID).
- **Medium (2.0):** Competitive market entries (M-Pesa).
- **Low (1.0):** Contextual milestones or infrastructure tweaks.

### 3. Historical Validation
- **Case Study:** Telebirr Launch (May 2021)
- **Observed Data:** Mobile money penetration (`ACC_MM_ACCOUNT`) rose from **4.7%** in 2021 to **9.45%** in 2024.
- **Result:** A total growth of **4.75 percentage points (pp)**. 
- **Calibration:** Given our model assigned Telebirr a "High" score of 3.0, our **Scaling Factor is 1.58pp per impact point**. This factor will be used to weight future predictions for 2026-2027.

### 4. Key Assumptions & Uncertainties
- **Independence:** We assume the impact of M-Pesa is independent of Telebirr, though in reality, they may compete for the same user base.
- **Confidence:** We have **High Confidence** in the impact of mobile money launches on Usage indicators. we have **Medium-Low Confidence** in the lag time for the National ID (Fayda) impact on Access, as the relationship between ID issuance and bank account opening is still emerging.