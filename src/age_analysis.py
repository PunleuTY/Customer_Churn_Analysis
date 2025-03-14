# Import Abstract Base Class
from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class AgeAnalysis(BaseAnalysis):

    # Since our dataset contains range of age between 18 - 65 so we need to categorize and initial label of them.
    # Bellow - [18-->30] : Young, [30-->50]: Middle-aged, [50-->65] : Olders
    def categorize_age_groups(self):
        bins = [17, 30, 50, 65]  # Define the age group ranges
        labels = ["Young", "Middle-aged", "Older"]
        self.df["Age Group"] = pd.cut(self.df["Age"], bins=bins, labels=labels, right=True)

    # This is the visualization function of churn rate which affected by age groups using matplotlib & seaborn to create barplot
    def visual_age_churn_by_group(self):
        plt.figure(figsize=(8, 5))
        sns.barplot(x = 'Age Group', y = 'Churn', data = self.df, estimator = lambda x: np.mean(x) * 100, palette = "coolwarm", hue = "Age Group")
        plt.title("Churn Rate by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Churn Rate (%)")

    # Function to returns the distribution of age         
    def age_distribution(self):
        return self.df["Age"].value_counts()
    
    # Function to visual the distribution of age frequency uses by using plt and syn libary to create hisplot
    def visual_age_distribution(self):
        plt.figure(figsize = (8, 5))
        sns.histplot(self.df['Age'], bins = 20, kde = True, color = "blue")
        plt.title("Age Distribution of Customers")
        plt.xlabel("Age")
        plt.ylabel("Frequency")

    # Function to print the churn rate(%) by age group
    def age_churn(self):
        result = self.df.groupby("Age", observed=True)["Churn"].mean() * 100
        print(result)
        return result
    
    # Function to visual the age and churn rateas a boxplot
    def visual_age_churn(self):
        plt.figure(figsize = (8, 5))
        sns.boxplot(x = 'Churn', y = 'Age', data = self.df, palette = "coolwarm", hue = "Churn")
        plt.title("Age vs. Churn Rate")
        plt.xlabel("Churn (0 = No, 1 = Yes)")
        plt.ylabel("Age")
    
    # Function to display all the analysis results
    def perform_analysis(self):

        # Display Age Distribution as a histplot
        print("Running Age Distribution Visualization : ")
        self.visual_age_distribution()

        # Display Churn Rate which affected by age without categorize and print as a boxplot
        print("Running Churn Rate by Age :")
        self.visual_age_churn()

        # Calling the categorize age function 
        self.categorize_age_groups()
        
        # Display churn rate by age_groups as a barplot
        print("\nChurn Rate by Age Group:\n", self.df.groupby("Age Group")["Churn"].mean() * 100)
        self.visual_age_churn_by_group()
    
        plt.show()

# Driver's code
if __name__ == "__main__":
    data_path = "data/data_500_rec.csv"
    age_analysis = AgeAnalysis(data_path)
    age_analysis.perform_analysis()
