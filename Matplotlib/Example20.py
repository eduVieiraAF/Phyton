# * Pie Charts

import matplotlib.pyplot as plt

y = ([45, 25, 15, 5, 10])
my_labels = (["Kotlin", "Python", "Java", "JavaScript", "TypeScript"])
my_explode = [0.1, 0.1, 0.1, 0.1, 0.1]

plt.pie(
    y,
    labels=my_labels,
    startangle=75,
    explode=my_explode,
    shadow=True,
    # labeldistance=0.5,
    wedgeprops={'linewidth': 3})
plt.legend(title="Top languages", loc="lower left", bbox_to_anchor=(-0.2, -0.1))
plt.show()
