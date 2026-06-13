
import matplotlib.pyplot as plt
import pandas as pd
from mplsoccer import Pitch


dataset.columns = dataset.columns.str.strip()

# pass and shot coordinates
coord_cols = ['location_x', 'location_y', 'pass_end_x', 'pass_end_y', 'shot_end_x', 'shot_end_y']
for col in coord_cols:
    dataset[col] = pd.to_numeric(dataset.get(col, pd.Series(dtype=float)), errors='coerce')

dataset = dataset.dropna(subset=['location_x', 'location_y'])

# \ pitch 
pitch = Pitch(pitch_type='statsbomb', pitch_color='#222222', line_color='#c7d5cc', stripe=False)
fig, ax = pitch.draw(figsize=(13, 9))

#  Plot passes AND shots
for index, row in dataset.iterrows():
    
  
    # If this row has a shot end coordinate, draw it as a shot
    if pd.notna(row.get('shot_end_x')) and pd.notna(row.get('shot_end_y')):
        outcome = str(row.get('shot_outcome', '')).lower()
        
        if 'goal' in outcome:
            event_color = 'green'
        else:
            event_color = 'red'
            
        ax.plot([row['location_x'], row['shot_end_x']], 
                [row['location_y'], row['shot_end_y']], 
                color=event_color, linewidth=3, alpha=1, zorder=1.5)
                
        pitch.scatter(row['location_x'], row['location_y'], 
                      ax=ax, color=event_color, edgecolors='black', marker='*', s=250, zorder=2)

   
    #  if it has a pass end coordinate, draw it as a pass
    elif pd.notna(row.get('pass_end_x')) and pd.notna(row.get('pass_end_y')):
        outcome = str(row.get('pass_outcome', '')).lower()
        
        if outcome == 'nan' or outcome == '' or outcome == 'none' or 'completed' in outcome:
            event_color = 'green'
        else:
            event_color = 'red'
            
        #  pass line
        ax.plot([row['location_x'], row['pass_end_x']], 
                [row['location_y'], row['pass_end_y']], 
                color=event_color, linewidth=2, alpha=1, zorder=1.5)
                
        
        pitch.scatter(row['location_x'], row['location_y'], 
                      ax=ax, color=event_color, edgecolors='black', s=140, zorder=2)

plt.show()
