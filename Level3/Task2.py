import pandas as pd
import matplotlib.pyplot as plt
def visualize_data():
    data = {
        "Name": ["Lavanya", "Sindhu", "Praneetha", "Afrida", "SaiLaxmi"],
        "Age": [20, 30, 35, 25, 28],
        "Salary": [55000, 60000, 75000, 85000, 65000]
    }    
    df = pd.DataFrame(data)
    plt.bar(df["Name"], df["Salary"], color="skyblue")
    plt.xlabel("Employee Name")
    plt.ylabel("Salary")
    plt.title("Salary Comparison")
    plt.show()
visualize_data()