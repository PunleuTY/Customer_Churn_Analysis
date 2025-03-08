from base_analysis import BaseAnalysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class ContractAnalysis(BaseAnalysis):
    def perform_analysis(self):
        print(f"\n Contract Length Distribution : \n{self.contract_ditribution()}")
        self.visual_contract_distribution()
        print(f"\n Churn Rate by Contract Length :\n {self.contract_churn()}")
        self.visual_contract_churn()

        plt.show()

    def contract_ditribution(self):
        return self.df["Contract Length"].value_counts()
    
    def visual_contract_distribution(self):
        plt.figure(figsize = (6,4))
        sns.countplot(x = "Contract Length", data = self.df, palette = "coolwarm", order = self.df['Contract Length'].value_counts().index )
        plt.title("Contract Length Distribution of Customers")
        plt.xlabel("Contract Length")
        plt.ylabel("Count")
        plt.show()
    
    def contract_churn(self):
        return self.df.groupby("Contract Length")['Churn'].mean() * 100
    
    def visual_contract_churn(self):
        plt.figure(figsize=(6,4))
        sns.barplot(x=self.contract_churn().index, y = self.contract_churn().values,palette="coolwarm")
        plt.title("Churn Rate by Contract Length")
        plt.xlabel("Contract Length")
        plt.ylabel("Churn Rate (%)")
        plt.ylim(0, 100)
        

if __name__ == "__main__":
    data_path = "../data/data_500_rec.csv"
    contract_analysis = ContractAnalysis(data_path)
    contract_analysis.perform_analysis()


