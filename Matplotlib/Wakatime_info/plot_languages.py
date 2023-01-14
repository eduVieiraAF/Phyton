import json
import matplotlib.pyplot as plt

# with open('Matplotlib\Wakatime_info\data.json') as file:
#    data = json.load(file)
#    labels = [item["name"] for item in data["data"]]
#    values = [item["percent"] for item in data["data"]]
#    colors = [item["color"] for item in data["data"]]
    
#    plt.pie(values, colors = colors, labels=values)
#    plt.legend(labels)
    
#    plt.show()

with open('Matplotlib\Wakatime_info\data.json') as json_file:
    data = json.load(json_file)
    labels = [item['name'] for item in data['data']]
    values = [item['percent'] for item in data['data']]
    colors = [item['color'] for item in data['data']]
    plt.title("Most used languages in the last 30 days")
    plt.barh(labels, values, color=colors)
    plt.xlabel('Percent')
    plt.ylabel('Language')
    plt.show()