import matplotlib.pyplot as plt
import json

with open('Matplotlib\Wakatime_info\days_hours.json') as file:
    data = json.load(file)
    
hours = [item["grand_total"]["hours"] for item in data["data"]]

dates = [item["range"]["date"] for item in data["data"]]

plt.pie(hours, labels=dates, autopct='%1.1f%%')
plt.title("Hours per day")
plt.show()