# a kwarg (short for keyword arguments) is a parameter that will pack all arguments into a dictionary

def hello(**kwargs):  # can name it differently, just use **
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Edu", middle="Phoenix", last="Vieira",
      age="40 years old", job="Dev")
