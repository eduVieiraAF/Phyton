# ? What is Pandas?
# * It's a library used for working with data sets with functions for analyzing, exploring, and manipulating data.
# It stands for "Panel Data",  and "Python Data Analysis".

import pandas as pd

my_dataset = {"data": [{"color": "#f1e05a", "name": "JavaScript", "percent": 42.77},
                       {"color": "#31859c", "name": "TypeScript", "percent": 19.47},
                       {"color": "#F18E33", "name": "Kotlin", "percent": 14.88},
                       {"color": "#e44b23", "name": "HTML", "percent": 9.57},
                       {"color": "#16ce40", "name": "JSON", "percent": 4.32},
                       {"color": "#dc9658", "name": "Text", "percent": 3.38},
                       {"color": "#563d7c", "name": "CSS", "percent": 3.15},
                       {"color": "#083fa1", "name": "Markdown", "percent": 0.9},
                       {"color": "#3581ba", "name": "Python", "percent": 0.73},
                       {"color": "#d62728", "name": "Git", "percent": 0.52},
                       {"color": "#9467bd", "name": "AUTO_DETECTED", "percent": 0.18},
                       {"color": "#8c564b", "name": "GitIgnore file", "percent": 0.07},
                       {"color": "#1f9aef", "name": "Other", "percent": 0.04},
                       {"color": "#aec7e8", "name": "IDEA_MODULE", "percent": 0.01},
                       {"color": "#e377c2", "name": "INI", "percent": 0.01}]}

my_data = pd.DataFrame(my_dataset)
print(pd.__version__)
print(my_data)
