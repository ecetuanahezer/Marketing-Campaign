Ad Campaign Data Generator and Analytics Demo

This repository contains a simple Python script to generate synthetic performance data for digital advertising campaigns and a Jupyter Notebook for basic analysis and anomaly detection.

The generated data simulates 90 days of daily metrics (Impressions, Clicks, Cost, Conversions, Installs, Revenue) for several campaigns targeting iOS, Android, and Retargeting audiences.

🚀 Project Structure

The project relies on two main files:

dummy_ads_data.py: A Python script (based on the code provided) that defines the campaign structure and generates the synthetic daily performance metrics.

analyze_dummy_data.ipynb: A Jupyter Notebook that loads the data from the script, performs aggregations, calculates key performance indicators (KPIs), and runs a basic time-series anomaly detection on the data.

🛠️ Requirements

To run the analysis notebook, you will need the following installed:

Python 3.x

Jupyter Notebook or JupyterLab

pandas (for data manipulation)

matplotlib (for plotting and visualization)

datetime (standard Python library)

You can install the necessary external libraries using pip:

pip install pandas matplotlib jupyter


📊 Data Overview

The generated data structures include:

1. Campaigns

A list of dictionaries defining the high-level campaigns.
| Key | Type | Description |
| :--- | :--- | :--- |
| id | int | Unique campaign ID. |
| name | str | Descriptive name (e.g., "App Install - IOS"). |
| status | str | Campaign status (e.g., "ENABLED", "PAUSED"). |

2. Ad Groups

A list of dictionaries detailing the groups under each campaign.
| Key | Type | Description |
| :--- | :--- | :--- |
| id | int | Unique ad group ID. |
| campaign_id | int | Links to the parent campaign. |
| name | str | Ad Group name (e.g., "iOS Search Ads"). |
| status | str | Ad Group status. |

3. Metrics

A list of daily performance metrics generated over 90 days for each ad group.
| Key | Type | Description |
| :--- | :--- | :--- |
| ad_group_id | int | Links to the parent ad group. |
| date | str | Date in YYYY-MM-DD format. |
| impressions | int | Number of times ads were shown. |
| clicks | int | Number of clicks on the ads. |
| cost | float | Total advertising spend. |
| conversions | int | Post-click user actions (e.g., sign-ups). |
| installs | int | App installations (a specific type of conversion). |
| revenue | float | Revenue generated from installs. |

🚀 How to Run the Analysis

Save the Data Generator: Ensure the provided Python code (which generates campaigns, ad_groups, and metrics) is saved as dummy_ads_data.py in your project directory.

Save the Analysis Notebook: Ensure the analysis notebook is saved as analyze_dummy_data.ipynb in the same directory.

Start Jupyter: Open your terminal in the project directory and run:

jupyter notebook


Open the Notebook: Click on analyze_dummy_data.ipynb in your browser.

Run Cells: Execute the cells sequentially to load the data, generate the summary tables, and visualize the KPI trends, including the anomaly detection plots.