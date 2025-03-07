# Customer Churn Analysis

## Project Structure
```plaintext
Customer_Churn_Analysis/
├── data/
│   └── data_500_rec.csv                   # Dataset 500 records
├── feature_analysis/
│   ├── base_analysis.py                   # Feature Analysis Abstract Base Class
│   ├── age_analysis.py                    # Age Analysis Feature
│   ├── gender_analysis.py                 # Gender Analysis Feature
│   ├── tenure_analysis.py                 # Tenure Analysis Feature
│   ├── usage_frequency_analysis.py        # Usage Frequency Analysis Feature
│   ├── support_call_analysis.py           # Support Call Analysis Feature
│   ├── payment_delay_analysis.py          # Payment Delay Analysis Feature
│   ├── subscription_analysis.py           # Subscription Analysis Feature
│   ├── contract_analysis.py               # Contract Analysis Feature 
│   ├── total_spend_analysis.py            # Total Spend Analysis Feature
│   ├── last_interaction_analysis.py       # Last Interaction Analysis Feature
│   ├── churn_analysis.py                  # Churn Analysis Feature
│   └── correlation_analysis.py            # Overall Correlation Analysis Feature
├── requirements.txt                       # Project Dependencies
├── main.ipynb                             # Main Python Notebook to run Analysis Features
└── README.md                              # Project Guide
```

## Getting Started
### Setup Workspace
- Clone the project: Copy the URL of the repository
```bash
git clone repo_url
```
- Create your own local branch: The commit will create a new branch and switch to it
```bash
git checkout -b "branch_name"
```
> **Note:** 
> - You should create a branch analysis feature
> - Branch Naming Convention: "Yourname/feature" separate by hypen " - "
- Download the dependencies
```bash
pip install -r requirements.txt
```
- Contribute to the project

## Commit to main Branch
Make sure you are on your own branch
- Add your change
```bash
git add .
```
- Commit Message
```bash
git commit -m "Message"
```
- Push to main branch
```bash
git push origin branch_name
```
- Go to the repository on GitHub
- Click on ``Compare & Pull Request`` option
- Define the name and description of your Pull Request
- Click on ``Create Pull Request``
- Request for reviewers to review and approve your Pull Request
- After approval, you can merge the code to ``main`` branch