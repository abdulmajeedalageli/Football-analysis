# Advanced Football Tactical Dashboard ⚽📊

A professional-grade football analytics dashboard that integrates Power BI's interactive cross-filtering with Python's advanced spatial mapping capabilities. This project transforms raw event data into broadcast-quality tactical visualizations, including pass networks, shot maps, density heatmaps, and match momentum charts.

---

## 📊 Tactical Dashboards
The Power BI dashboard is built on a Star Schema, allowing coaches and scouts to instantly filter tactical maps by individual players and event types. 

**Forward Profile: Kylian Mbappé**
![Kylian Mbappe Tactical Flow Map](assets/mbappe_tactical_map.png)

**Midfield Profile: Alexis Mac Allister**
![Alexis Mac Allister Passing Network](assets/mac_allister_passing_network.png)

*(Note: Ensure your high-resolution screenshots are uploaded to the `assets` folder in this repository to render above).*

---

## 🛠️ Tech Stack
* **Business Intelligence:** Power BI (Data Modeling, Slicers, Native Visuals)
* **Data Processing & Analytics:** Python, Pandas, DAX
* **Spatial Visualization:** matplotlib, mplsoccer, seaborn
* **Database:** SQLite (1-to-Many Relational Model)

---

## 🌟 Key Features & Analytical Approach

### 1. Broadcast-Quality Spatial Mapping (Python)
Instead of relying on static, misaligned background images, this dashboard uses the `mplsoccer` Python library to mathematically generate an exact 120x80 'Statsbomb' coordinate pitch natively inside Power BI.
* **Dark Mode Aesthetics:** A high-contrast charcoal (#222222) pitch with silver lines (#c7d5cc) reduces eye strain and makes data points stand out.
* **Pass Networks:** Maps successful passes (Green) and incomplete passes (Red) with accurate starting and ending vector lines.
* **Universal Shot/Pass Logic:** Dynamically distinguishes between passes and shots. Shots are highlighted using thicker lines and a distinct "Star" marker, conditionally colored by outcome (Goal vs. Miss/Save).

### 2. Player Territory Heatmaps
Utilizes Kernel Density Estimation (KDE) via the `seaborn` library to generate smooth, glowing heatmaps using the 'magma' color scale. This visually highlights a player's primary zones of influence, tactical positioning, and spatial dominance.

### 3. Native Power BI Analytics (DAX)
* **True Pass Completion KPI:** Accounts for industry-standard blank variables in professional event data (where successful actions are often left blank). Uses DAX to calculate an exact Pass Completion Percentage.
* **Match Momentum:** Groups event data into 15-minute tactical "bins" to display the volume of actions and success rates across the full 90 minutes. This chart is strictly filtered to prevent off-ball events from artificially inflating possession metrics.

### 4. Full Interactivity
The dashboard utilizes Power BI's native cross-filtering engine. Selecting a specific player from a slicer, or clicking a specific 15-minute window on the momentum chart, automatically filters the underlying dataset and instantly redraws the Python spatial map for that exact match scenario.

---

## ⚙️ Data Architecture & Modeling
To ensure the dashboard runs quickly and filters accurately, the underlying data model was streamlined using a highly efficient Star Schema. 

* **Simplified Structure:** Removed redundant tables in favor of a clean schema using just the core Fact table and Dimension table.
* **Fact_Events:** Contains raw match data, including exact `location_x`, `location_y`, `pass_end_x`, `pass_end_y`, `shot_end_x`, `shot_end_y`, and outcome text.
* **Dim_Players:** Dimension table containing player IDs and names, maintaining a 1-to-Many relationship with the Fact table to allow instant global dashboard filtering.
* **Data Cleaning Logic:** Built robust logic during the ETL phase to recognize `BLANK()`, "nan", and "Completed" as successful outcomes, ensuring Python and Power BI calculate accuracy flawlessly.
