from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class SubscriptionAnalysis(BaseAnalysis):
    
    # Function to return the subscription distribution 
    def subscription_distribution(self):
        return self.df["Subscription Type"].value_counts()
    
    # Function to display the subscription type distribution as a countplot
    def visual_subscription_distribution(self):
        plt.figure(figsize = (6,4))
        sns.countplot(x = "Subscription Type", data = self.df, palette = "coolwarm", hue = "Subscription Type", order = self.df['Subscription Type'].value_counts().index )
        plt.title("Subscription Type Distribution of Customers")
        plt.xlabel("Subscription Type")
        plt.ylabel("Count")
        

    # Function to return the percentage of subscription type
    def subscription_churn(self):
        return self.df.groupby("Subscription Type")["Churn"].mean() * 100
    
    # Function to display churn rate which affected by subscription type as a barplot
    def visual_subscription_churn(self):
        plt.figure(figsize = (6,4))
        sns.barplot(x = self.subscription_churn().index, y = self.subscription_churn().values, hue = self.subscription_churn().index, palette = "coolwarm")
        plt.title("Churn Rate by Subscription Type")
        plt.xlabel("Subscription Type")
        plt.ylabel("Churn Rate (%)")
        plt.ylim(0, 100)

    # Display all the analysis performance 
    def perform_analysis(self):
        # Display the subscription type distrinbution
        print(f"\n Subscription Type Distribution : \n{self.subscription_distribution()}")
        # Display a countplot to show the subscription type distribution
        self.visual_subscription_distribution()
        # Display Churn rate which affected by subscription type
        print(f"\n Churn Rate by Subscription Type :\n {self.subscription_churn()}")
        self.visual_subscription_churn()

        plt.show()


if __name__ == "__main__":
    data_path = "../data/data_500_rec.csv"
    subscriptionType_analysis = SubscriptionAnalysis(data_path)
    subscriptionType_analysis.perform_analysis()