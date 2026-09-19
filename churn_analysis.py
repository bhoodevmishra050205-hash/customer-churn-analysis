import pandas as pd
import matplotlib.pyplot as plt

print("Customer Churn Analysis Project")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Churn": [45, 38, 52, 30]
})

plt.plot(data["Month"], data["Churn"], marker="o")
plt.title("Monthly Customer Churn")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.savefig("images/churn_trend.png")

print(data)
