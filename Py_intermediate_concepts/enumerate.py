
tasks = ["walk the dog", "clean the house", "call mom", "write code", "eat healthy"]

# * this is fine but enumerate is better
# for i in range(len(tasks)):
#     task = tasks[i]
#     print(f"{i + 1}. {task}")

# * enumerate is better
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
    
# simple use
print(list(enumerate(tasks)))