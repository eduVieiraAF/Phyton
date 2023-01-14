import random

# List of 32 teams
teams = ['Argentina', 'Australia', 'Belgium', 'Brazil', 'Colombia', 'Costa Rica', 'Croatia', 'Denmark', 'Egypt', 
         'England', 'France', 'Germany', 'Iceland', 'Iran', 'Japan', 'Mexico', 'Morocco', 'Nigeria', 'Panama', 
         'Peru', 'Poland', 'Portugal', 'Russia', 'Saudi Arabia', 'Senegal', 'Serbia', 'South Korea', 'Spain', 
         'Sweden', 'Switzerland', 'Tunisia', 'Uruguay']

# Shuffle the list of teams
random.shuffle(teams)

# Divide the teams into 8 groups
group_a = teams[:4]
group_b = teams[4:8]
group_c = teams[8:12]
group_d = teams[12:16]
group_e = teams[16:20]
group_f = teams[20:24]
group_g = teams[24:28]
group_h = teams[28:]

# Print the groups
print(f'Group A: {group_a}')
print(f'Group B: {group_b}')
print(f'Group C: {group_c}')
print(f'Group D: {group_d}')
print(f'Group E: {group_e}')
print(f'Group F: {group_f}')
print(f'Group G: {group_g}')
print(f'Group H: {group_h}')

