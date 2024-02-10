# backend/main.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_plots(expenses, incomes):
    # Process data
    data = {'Expenses': expenses, 'Incomes': incomes}
    df = pd.DataFrame(data)

    # Generate plots
    plt.figure(figsize=(10, 5))
    df.plot(kind='bar')
    plt.title('Financial Tracker')
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('frontend/plot.png')

if __name__ == "__main__":
    expenses = [float(input(f"Enter expense {i+1}: ")) for i in range(5)]
    incomes = [float(input(f"Enter income {i+1}: ")) for i in range(5)]
    generate_plots(expenses, incomes)
