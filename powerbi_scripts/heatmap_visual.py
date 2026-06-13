
import matplotlib.pyplot as plt
import pandas as pd
from mplsoccer import Pitch

dataset.columns = dataset.columns.str.strip()
dataset['location_x'] = pd.to_numeric(dataset['location_x'], errors='coerce')
dataset['location_y'] = pd.to_numeric(dataset['location_y'], errors='coerce')
dataset = dataset.dropna(subset=['location_x', 'location_y'])

#  pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='#222222', line_color='#c7d5cc', stripe=False)
fig, ax = pitch.draw(figsize=(13, 9))

#  Heatmap
pitch.kdeplot(
    dataset['location_x'], 
    dataset['location_y'], 
    ax=ax,
    fill=True,
    levels=100,      
    cmap='magma',    
    alpha=0.75,      
    zorder=1
)


plt.show()
