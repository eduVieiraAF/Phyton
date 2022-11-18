# * Pie Charts

import matplotlib.pyplot as plt

y = ([45, 25, 25, 5])
my_labels = (["Kotlin", "Python", "Java", "JavaScript"])
my_explode = [0.2, 0.1, 0.1, 0.1]

plt.pie(y, labels=my_labels, startangle=180, explode=my_explode, shadow = True )
plt.legend(title = "Top languages")
plt.show()
