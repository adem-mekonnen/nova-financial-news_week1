# nova-financial-news_week1
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
│   ├── 1_eda_news.ipynb     # Task 1: Exploratory Data Analysis & NLP
│   ├── 2_technical_analysis.ipynb # Task 2: Financial Indicators (TA-Lib)
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
🚀 Task 1: Exploratory Data Analysis (EDA) & Git Setup
The first phase of the project focused on setting up a robust engineering environment and understanding the FNSPID (Financial News and Stock Price Integration Dataset).
1. Environment & CI/CD
Version Control: Implemented a strict branching strategy (main, task-1).
CI/CD: Configured GitHub Actions to run pytest on every push, ensuring code stability.
Dependencies: Managed via venv, with specific handling for TA-Lib binary installations on Windows.
2. Data Analysis Findings
We analyzed over 1.4 million headlines to understand publication trends.
📅 Time Series Trends
Data Anomaly: The dataset shows a massive exponential spike in article volume starting in 2019, peaking in 2020. Historical data from 2011–2018 is sparse.
Implication: Predictive models should prioritize post-2019 data to accurately reflect modern market volatility.
⏰ Intraday Publication Timing
Pattern: News publication follows a bimodal distribution aligned with US Market hours.
Spikes:
Pre-Market: 08:00 AM – 09:30 AM EST (Highest volume).
After-Hours: 04:00 PM EST.
Insight: Publishers strategically time releases to maximize impact on opening/closing prices.
✍️ Publisher Analysis
Concentration: The dataset is dominated by a small group of aggregators.
Top Publishers: Benzinga Staff, Lisa Levin, and Paul Quintaro account for a significant percentage of total headlines.
Topic Modeling (LDA): Headlines cluster into three main categories:
Earnings: (Keywords: EPS, Revenue, Beat, Q3)
Analyst Ratings: (Keywords: Upgrade, Downgrade, Price Target)
Corporate Action: (Keywords: Acquisition, Agreement, FDA)
🛠 Installation & Setup
Clone the repository:
code
Bash
git clone https://github.com/adem-mekonnen/nova-financial-news_week1.git
cd nova-financial-news_week1
Create a Virtual Environment:
code
Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:
code
Bash
pip install -r requirements.txt
Note for Windows Users: If TA-Lib fails to install, download the binary wheel from here and install it manually.
Run the Analysis:
Launch Jupyter Lab or VS Code to view notebooks/1_eda_news.ipynb.
