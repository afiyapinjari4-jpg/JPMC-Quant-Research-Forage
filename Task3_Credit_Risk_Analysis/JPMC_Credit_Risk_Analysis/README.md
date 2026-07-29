\# Credit Risk Analysis - JPMorgan Quant Research Forage



\## Project Overview



This project focuses on building a machine learning model to predict the probability of loan default for borrowers.



The objective is to assist a retail banking team in identifying high-risk customers by estimating their Probability of Default (PD).



\---



\## Business Problem



Banks need accurate methods to evaluate borrower risk before approving loans.



This project uses historical customer financial data to build a classification model that predicts whether a borrower is likely to default.



\---



\## Dataset



The dataset contains 10,000 customer records with the following features:



\- customer\_id

\- credit\_lines\_outstanding

\- loan\_amt\_outstanding

\- total\_debt\_outstanding

\- income

\- years\_employed

\- fico\_score

\- default (Target Variable)



Target:



\- 0 → No Default

\- 1 → Default



\---



\## Data Analysis



Performed:



\- Dataset inspection

\- Missing value analysis

\- Target distribution analysis

\- Feature selection



Missing values:



\- No missing values found



Default distribution:



\- No Default: 8149 customers

\- Default: 1851 customers



\---



\## Feature Engineering



Removed:



\- customer\_id



Reason:



customer\_id is only an identifier and does not contribute to prediction.



Final features used:



\- credit\_lines\_outstanding

\- loan\_amt\_outstanding

\- total\_debt\_outstanding

\- income

\- years\_employed

\- fico\_score



\---



\## Machine Learning Model



Model Used:



\*\*Logistic Regression\*\*



Reason:



Logistic Regression is widely used in credit risk modelling because it provides probability estimates and good interpretability.



\---



\## Model Training



Dataset split:



\- Training Data: 80%

\- Testing Data: 20%



Training samples:



8000



Testing samples:



2000



\---



\## Model Performance



\### Accuracy



