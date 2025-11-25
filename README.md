Here is the complete, updated **README.md** file. It now includes the details for **Task 2 (Technical Analysis)** and **Task 3 (Correlation)**, making it a complete representation of your Week 1 work.

You can copy and paste this directly into your `README.md` file.

***

```markdown
# Predicting Stock Price Moves with News Sentiment 📈

**Business Objective:**  
Nova Financial Solutions aims to enhance its predictive analytics capabilities by analyzing financial news sentiment. This project seeks to establish statistical correlations between news sentiment and stock price movements to generate actionable investment strategies.

![Build Status](https://github.com/adem-mekonnen/nova-financial-news_week1/actions/workflows/unittests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

## 📂 Project Structure

The repository is organized to support reproducible data science workflows, separating data, analysis notebooks, and production-ready code.

```text
├── .github/
│   └── workflows/
│       └── unittests.yml    # CI/CD pipeline for automated testing
├── .vscode/
│   └── settings.json        # Workspace settings
├── notebooks/
│   ├── 1_eda_news.ipynb           # Task 1: Exploratory Data Analysis & NLP
│   ├── 2_technical_analysis.ipynb # Task 2: Financial Indicators (TA-Lib)
│   ├── 3_correlation_analysis.ipynb # Task 3: Sentiment vs. Return Correlation
│   └── README.md
├── scripts/                 # Standalone scripts for data fetching/processing
├── src/
│   ├── __init__.py
│   └── loader.py            # Helper functions for data loading
├── tests/
│   ├── __init__.py
│   └── test_basic.py        # Unit tests for CI/CD validation
├── .gitignore               # Ignores large data files and environments
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

> **Note:** The raw dataset (`raw_analyst_ratings.csv`) is excluded from the repository via `.gitignore` due to file size limits (>300MB).

---

## 🚀 Task 1: Exploratory Data Analysis (EDA) & Git Setup

The first phase focused on establishing a robust engineering environment and understanding the **FNSPID (Financial News and Stock Price Integration Dataset)**.

### 1. Environment & CI/CD
*   **Version Control:** Implemented a strict branching strategy (`main`, `task-1`, `task-2`, `task-3`).
*   **CI/CD:** Configured GitHub Actions to run `pytest` on every push, ensuring code stability.
*   **Dependencies:** Managed via `venv`, with specific handling for `TA-Lib` binary installations on Windows.

### 2. Data Analysis Findings
We analyzed over **1.4 million headlines** to understand publication trends.
*   **📅 Time Series Anomaly:** The dataset shows an exponential spike in article volume starting in **2019**, peaking in **2020**.
*   **⏰ Intraday Timing:** News publication follows a bimodal distribution aligned with market hours. Spikes occur at **08:00–09:30 AM EST** (Pre-Market) and **04:00 PM EST** (After-Hours).
*   **✍️ Publisher Concentration:** Top publishers like *Benzinga* and *Paul Quintaro* dominate the feed.
*   **🔍 Topic Modeling:** Headlines cluster into *Earnings Reports*, *Analyst Ratings*, and *Corporate Actions*.

---

## 📈 Task 2: Quantitative Technical Analysis

To establish "Ground Truth" for market movements, we retrieved historical stock data using `yfinance` and calculated key technical indicators using **TA-Lib**.

### Key Indicators Implemented:
*   **SMA (Simple Moving Average):** Calculated the 20-day SMA to identify short-term trend directions.
*   **RSI (Relative Strength Index):** Used to detect overbought (>70) and oversold (<30) conditions.
    *   *Insight:* RSI proved effective in flagging potential reversals during high-news-volume days.
*   **MACD (Moving Average Convergence Divergence):** Computed to identify momentum shifts before they appear in raw price action.

---

## 🔗 Task 3: Correlation Analysis

The core objective was to statistically measure the predictive power of news sentiment.

### Methodology
1.  **Sentiment Scoring:** Applied `TextBlob` to generate polarity scores (-1 to +1) for every headline.
2.  **Date Alignment:** Normalized timestamps and aggregated multiple daily headlines into a `Daily_Average_Sentiment`.
3.  **Statistical Testing:** Calculated the **Pearson Correlation Coefficient** between Daily Sentiment and Daily Stock Returns.

### 💡 Key Findings
*   **Weak Positive Correlation:** The correlation coefficient for major tickers (e.g., AAPL) ranged between **0.05 and 0.12**.
*   **Interpretation:** While good news generally aligns with positive returns, the relationship is not linear.
*   **"Buy the Rumor":** We observed instances of high positive sentiment followed by negative returns, suggesting market pricing often precedes news publication.

---

## 🛠 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/adem-mekonnen/nova-financial-news_week1.git
    cd nova-financial-news_week1
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note for Windows Users: If `TA-Lib` fails to install via pip, download the binary wheel from [here](https://github.com/cgohlke/talib-build/releases) and install it manually.*

4.  **Run the Analysis:**
    Launch Jupyter Lab or VS Code to view the notebooks in the `notebooks/` directory.

---
**Author:** Adem Mekonnen
**Date:** November 2025
```
