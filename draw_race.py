# Data wrangling 
import pandas as pd 

# Barplot race drawing
import bar_chart_race as bcr

# Random simulation 
import numpy as np

# OS traversal 
import os 

# Import dates
import time

# Configuration reading 
import yaml

# Reading the configuration file 
conf = yaml.load(open("conf.yml", encoding='utf8'), Loader=yaml.FullLoader)

# Loading the hyperparameters
# Number of iterations 
n = conf.get('n_simulations')

# The total runtime of the video in seconds
total_runtime = conf.get('total_runtime')

# Image quality
dpi = conf.get('dpi')

# Number of bars to display on the graph 
n_bars = conf.get('n_bars')

# Final figure size 
figsize = conf.get('figsize')
figsize = (figsize[0], figsize[1])

# Reading the data 
names = pd.read_excel('data/names_input.xlsx')

# Droping missing rows 
names.dropna(inplace=True)

# Concatenating the names 
names['full_name'] = names['name'] + ' ' + names['surname']

# Adding the initial wining values 
names['n_wins'] = 0

# Converting to wide format 
names = names.pivot_table(columns='full_name', values='n_wins')

# Extracting name list 
name_list = names.columns.values.tolist()
print(f"Number of participants: {len(name_list)}")

# Calculating the period length (in ms) for the video to be equal to total_runtime
period_length = ( total_runtime / n ) * 1000

start = time.time()

# Placeholder dataframe 
i = 0
while (i < n) or (np.sum(last_counts == np.max(last_counts)) != 1):
    # Extracting the winner 
    winner = np.random.choice(name_list, 1)[0]

    # Getting the index of the winner 
    winner_index = np.where([x == winner for x in name_list])[0][0]

    # Getting the last result 
    last_counts = names.iloc[i, ]

    # Updating the winner count 
    last_counts[last_counts.index == winner] = last_counts[last_counts.index == winner] + 1

    # Appending to the names df 
    names = names.append(last_counts)

    # Adding to the iteration 
    i += 1

# Reseting the index 
names.reset_index(inplace=True, drop=True)
print(f"Made simulations in: {time.time() - start} seconds")

# Making the output dir 
if not os.path.isdir('output'):
    os.mkdir('output')

# Visualizing
start = time.time()
bcr.bar_chart_race(
    df=names,
    filename=f'output/barplot_race-{time.time()}.mp4',
    steps_per_period=10,
    n_bars=n_bars,
    period_length=period_length,
    cmap='pastel2',
    title='"Scorify" partnerių vakaro žaidimas',
    dpi=dpi,
    fixed_max=True,
    interpolate_period=True,
    figsize=figsize
    ) 
print(f"Drew in: {time.time() - start} seconds")