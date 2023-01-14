import matplotlib.pyplot as plt
import json

with open('Matplotlib\Wakatime_info\days_hours.json') as file:
    data = json.load(file)
    
hours = [item["grand_total"]["hours"] for item in data["data"]]
dates = [item["range"]["date"] for item in data["data"]]

plt.bar(dates, hours, color="#00748e" )
plt.xlabel("Dates")
plt.ylabel("Hours")
plt.title("Hours per day")

plt.show()