# Key Insights: Exploratory Data Analysis

**Analyst:** Rufta

### 1. The Access-Usage Paradox (2021-2024)

There is a stark divergence between infrastructure adoption and service utilization. While Mobile Money (Usage) saw a massive surge following the launch of Telebirr, general Account Ownership (Access) experienced a notable slowdown.

* **Evidence:** The "Slowdown Area" in your line chart shows `ACC_OWNERSHIP` grew only **3 percentage points** (46% to 49%) between 2021 and 2024. In contrast, the secondary Y-axis for `USG_P2P_VALUE` shows an **exponential slope**, moving from near-zero to becoming a dominant transaction medium.
* **Reasoning:** This confirms that while the "unbanked" are not necessarily becoming "banked" in the traditional sense, existing users are transacting at much higher velocities. The barrier to entry for new users likely remains high due to smartphone costs (as noted by your `INF_SMP_OWN` observation).

### 2. Event Impact: The "Telebirr Shock"

The timeline analysis identifies the May 2021 Telebirr launch as the primary structural break in Ethiopia's financial history.

* **Evidence:** Your timeline visualization shows an immediate vertical pivot in `ACC_MM_ACCOUNT` following the **Telebirr Launch** event. The entry of **Safaricom M-Pesa (2023)** acts as a "booster" rather than a primary catalyst, primarily driving the **P2P Transfer Value** (`USG_P2P_VALUE`) rather than account counts.
* **Significance:** This suggests that the market has moved from an *acquisition* phase (2021-2022) to a *deepening* phase (2023-present).

### 3. Structural Gender Gap Persistence

Despite the digital revolution, the gender gap remains stubbornly static, suggesting that digital tools alone are not a "silver bullet" for equality.

* **Evidence:** The `GEN_GAP_ACC` bar chart shows that the gap has not narrowed significantly in the 2021-2024 window, despite the overall increase in mobile money accounts.
* **Reasoning:** Men are typically the first to adopt new mobile technology in Ethiopia due to higher levels of smartphone ownership and disposable income, leaving women in a "digital lag" period.

### 4. Data Quality & Coverage Assessment

The dataset is now robust enough for forecasting, but requires careful handling of "silent" pillars.

* **Quality Metrics:** Your Quality Summary identifies **0 Low Confidence Records**, which is excellent for model reliability.
* **Limitations:** * **Missing Values (19):** These are concentrated in `impact_link` and `target` types, which is expected as they represent relationships rather than historical observations.
* **Pillar Gaps:** 13 records have no pillar, mostly events. This supports your decision to keep events "pillar-neutral" so they can influence both Access and Usage.

### 5. Transition to Digital Dominance (The Crossover)

The data reflects a pivot point where digital P2P transfers began outstripping traditional cash-based metrics (ATM usage).

* **Insight:** The `USG_P2P_VALUE` growth is now the primary driver of the entire FI ecosystem. The "Usage" pillar is effectively "pulling" the "Access" pillar forward; people are now opening accounts specifically to participate in the digital P2P economy rather than for savings or credit.