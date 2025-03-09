from base_analysis import BaseAnalysis

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class GenderAnalysis(BaseAnalysis):
    def perform_analysis(self):
        # Load dataset
        df = self.load_data()
        # Gender distribution
        gender_counts = df["Gender"].value_counts()
        print("Gender Count: ")
        print(f"Male: {gender_counts["Male"]}")
        print(f"Female: {gender_counts["Female"]}")
        
        # Gender Distribution visualization
        self.gender_count_visualization(df)
        
        # Churn rate for each group
        gender_churn_rate = df.groupby("Gender")["Churn"].mean() * 100
        print("\nGender Churn Rate: ")
        print(f"Male: {gender_churn_rate["Male"]:.2f}%")
        print(f"Female: {gender_churn_rate["Female"]:.2f}%")
        
        # Churn Rate visualization
        self.gender_churn_rate_visualization(gender_churn_rate)
    
    def gender_count_visualization(self, df):
        plt.figure(figsize = (6, 4))
        sns.countplot(x = "Gender", data = df, palette = "pastel", hue = "Churn")
        plt.title("Gender Distribution of Customers")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plt.show()
        
    def gender_churn_rate_visualization(self, gender_churn_rate):
        # Plot Churn Rate by Gender
        plt.figure(figsize=(8, 5))
        sns.barplot(x = gender_churn_rate.index, y = gender_churn_rate.values, hue = gender_churn_rate.index , palette = "coolwarm", legend = True)
        plt.title("Churn Rate by Tenure Group")
        plt.ylabel("Churn Rate (%)")
        plt.xlabel("Tenure Group")
        plt.ylim(0, 100)
        plt.show()

if __name__ == "__main__":
    path = "data/data_500_rec.csv"
    gender_analysis = GenderAnalysis(path)
    gender_analysis.perform_analysis()