# Task 4 - FICO Score Bucketing

## Overview
This project implements FICO score bucketing for mortgage risk analysis as part of the JPMC Quantitative Research Virtual Experience.

## Objective
- Categorize continuous FICO scores into rating buckets.
- Assign lower ratings to customers with better credit scores.
- Calculate the Probability of Default (PD) for each rating bucket.

## Method
- Load the customer loan dataset.
- Divide FICO scores into 10 equal-frequency buckets using pandas `qcut`.
- Reverse bucket numbering so Rating 1 represents the highest FICO scores.
- Compute:
  - Minimum FICO score
  - Maximum FICO score
  - Number of customers
  - Number of defaults
  - Probability of Default (PD)

## Output Files
- `fico_rating_map.csv` – Rating summary with PD.
- `fico_bucketed_data.csv` – Original data with assigned ratings.

## Technologies Used
- Python
- Pandas