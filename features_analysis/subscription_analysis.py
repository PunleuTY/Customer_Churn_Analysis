from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class SubscriptionAnalysis(BaseAnalysis):
    
    def perform_analysis(self):
        print(f"\n Subscription Type Distribution : \n{self.subscription_distribution()}")
        self.visual_subscription_distribution()
        print(f"\n Churn Rate by Subscription Type :\n {self.subscription_churn()}")
        self.visual_subscription_churn()

        plt.show()

    def subscription_distribution(self):
        return self.df["Subscription Type"].value_counts()
    
    def visual_subscription_distribution(self):
        plt.figure(figsize = (6,4))
        sns.countplot(x = "Subscription Type", data = self.df, palette = "coolwarm", order = self.df['Subscription Type'].value_counts().index )
        plt.title("Subscription Type Distribution of Customers")
        plt.xlabel("Subscription Type")
        plt.ylabel("Count")
        plt.show()

    def subscription_churn(self):
        return self.df.groupby("Subscription Type")["Churn"].mean() * 100
    
    def visual_subscription_churn(self):
        plt.figure(figsize=(6,4))
        sns.barplot(x=self.subscription_churn().index, y = self.subscription_churn().values,palette="coolwarm")
        plt.title("Churn Rate by Subscription Type")
        plt.xlabel("Subscription Type")
        plt.ylabel("Churn Rate (%)")
        plt.ylim(0, 100)

if __name__ == "__main__":
    data_path = "../data/data_500_rec.csv"
    subscriptionType_analysis = SubscriptionAnalysis(data_path)
    subscriptionType_analysis.perform_analysis()