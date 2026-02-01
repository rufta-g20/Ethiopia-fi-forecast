# Key Insights: Exploratory Data Analysis
**Analyst:** Rufta

### 1. The Access-Usage Paradox (2021-2024)
While Mobile Money (Usage) saw a massive spike following the launch of Telebirr (2021) and M-Pesa (2023), general Account Ownership (Access) only grew by 3 percentage points. 
**Evidence:** `ACC_OWNERSHIP` rose from 46% to 49%, while `ACC_MM_ACCOUNT` and transaction volumes show exponential growth on the secondary Y-axis.
**Reasoning:** The "registered vs. active" gap is significant. Many accounts are opened to receive specific one-off transfers but aren't utilized for daily financial life due to high smartphone costs and limited merchant acceptance.

### 2. Gender Gap Persistence
The gender gap remains a structural barrier to full inclusion.
**Evidence:** Analysis of `GEN_GAP_ACC` indicates that males continue to lead females by ~10-15%, with digital-only accounts (`GEN_MM_SHARE`) showing a similar skew.

### 3. Event Impact: Telebirr vs. M-Pesa
The timeline visualization confirms that the Telebirr launch (May 2021) was the single largest catalyst for the surge in `ACC_MM_ACCOUNT` in the dataset. M-Pesa's entry (2023) has accelerated the usage of interoperable P2P transfers.

### 4. Data Quality & Coverage Assessment
**Limitations:** - **Sparsity:** Infrastructure data (e.g., `ACC_4G_COV`) is sparse before 2020, making long-term correlation analysis difficult.
- **Missing Values:** 14 records are missing `value_numeric`, primarily in target or impact_link record types.
- **Confidence:** 100% of analyzed records are 'High' or 'Medium' confidence, providing a solid foundation for Task 3 modeling.

### 5. Transition to Digital Interoperability
The data reflects a pivot point in 2024 where digital P2P transfers (`USG_P2P_VALUE`) began outstripping traditional cash-based metrics, suggesting that the "Usage" pillar is now driving the "Access" pillar.