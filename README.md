## Classification-Model-Project

## Goal
* The purpose of this model is to predict customer churn at Telco.
* My goal is to find specific features that drive customer churn at Telco.

## Initial hypotheses

* Null Hypothesis: contract type and monthly charges features do not drive customers to churn
* Alternative Hypothesis: contract type and monthly charges features do drive customers to churn

## Data dictionary

contract_type: The type of contract the customer has agreed to

paperless_billing: Whether the customer utilizes paperless billing or not

senior_citizen: Whether or not customer is a senior citizen

partner: Whether or not the customer has a partner

dependents: Whether or not the customer has dependents	

monthly_charges: How much the customers pays for service monthly	

multiple_lines: Whether or not the customer has multiple lines	

online_security: Whether or not the customer has online security	

online_backup: Whether or not the customer has online backup

device_protection: Whether or not the customer has device protection

tech_support: Whether or not the customer has tech support	

streaming_tv: Whether or not the customer streams tv

streaming_movies: Whether or not the customer streams movies or not	

internet_service_type: Type of internet service the customer has

payment_type: Type of payment the customer uses

## Planning:
- Generate questions to ask about the data set based off of what I want my model to predict. Do any features have an impact on churn?. What features significantly drive customer churn. It should predict customer churn.
- Determine the format. Final report should be in .ipynb, Modules should be in .py, Predictions should be in .csv.
- Determine audience and develop speech and presention accordingly. Audience will be lead data scientist.
- Determine correlation between features and customer churn
- Develop my null hypothsisis and alternative hypothesis. 
- Determine what model to create
  
## Acquisition:
- Using a function with my credentials stored in a env.py file, I connected to codeup's MySQL server.
- Created a query pertinent to the project
- Using a deliverable I created with the query, I called a function I built to acquire and read telco data from codeup's MySQL server.

## Preparation:
- perform tasks such as handling null values, outliers, normalizing text, binning of data, changing data types, etc.
- I dropped columns, changed data types.

## Exploration & pre-processing:
- Made visuals and used stats to understand which features had a significant correalation, relationship
- I dropped features that had no significance

## Modeling:
- I choose a classification random forest model
- I used my train data set to train my model
- I made predictions with my model
- I made multple models and choose the best one

## Delivery:
- Deployed my model and a reproducable report
- Made recommendations

## Key findings, recommendations, and takeaways
- Monthly contracts amd charges are key features driving customer churn
- I recommend incentivizing yearly contracts by offering promotion deals and a loyalty program

## Instructions or an explanation of how someone else can reproduce project and findings

Enviroment setup: 
- Install Conda, Python, MySql, VS Code or Jupyter Notebook
- Clone this repo 
