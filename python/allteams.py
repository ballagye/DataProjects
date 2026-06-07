
# Imports
import os  # Path vers le dataset
import polars as pl  # Manipuler les données du dataset
import matplotlib.pyplot as plt  # Visualiser les données

# Création de la DataFrame et cleaning
_here = os.path.dirname(os.path.abspath(__file__))
df = pl.DataFrame(pl.read_csv(os.path.join(_here, "../data/NBA_DATASET/shootingdataperteam.csv")))
                  
df = df.drop("Unnamed: 0")

years = df[3, 1::4]
years = years.to_numpy()
years = years.flatten()

teams = df[5:35, 0]
teams = teams.to_numpy()

threePointsMade = df[5:35, 1::4]
threePointsMade = threePointsMade.to_numpy()

threePointsAttempts = df[5:35, 2::4]
threePointsAttempts = threePointsAttempts.to_numpy()

threePointsPercent = df[5:35, 3::4]
threePointsPercent = threePointsPercent.to_numpy()

new_df = pl.DataFrame({
    "Teams": teams,
    "3PA": threePointsAttempts,
    "3PM":  threePointsMade,
    "3P%": threePointsPercent
})

new_df = new_df.explode("3PM","3PA","3P%")

new_df = new_df.with_columns(
    pl.col("3PM","3PA","3P%").cast(pl.Float64, strict=False)
)

print(new_df)

colors = ["#E03A3E", "#007A33", "#000000", "#CC0000", "#860038", "#00538C", "#0E2240", "#1D42BA", "#1D428A", "#CE1141", "#002D62", "#C8102E", "#552583", "#5D76A9", "#98002E", "#00471B", "#236192", "#006BB6", "#EF3B24", "#0077C0", "#003DA5", "#E56020", "#E8472A", "#5A2D81", "#C4CED4", "#A6192E", "#F9A01B", "#002B5C", "#1D1160", "#0C2340"]

teams_ordered = teams.flatten().tolist()
color_map = {team: colors[i] for i, team in enumerate(teams_ordered)}

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 18))

for team in teams_ordered:
    team_data = new_df.filter(pl.col("Teams") == team)
    c = color_map[team]
    ax1.plot(years, team_data["3PM"], color=c, label=team)
    ax2.plot(years, team_data["3PA"], color=c, label=team)
    ax3.plot(years, team_data["3P%"], color=c, label=team)

ax1.set_title("Nombre de 3 points réalisés")
ax2.set_title("Nombre de 3 points tentés")
ax3.set_title("Pourcentage de 3 points")

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

ax1.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=7)
ax2.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=7)
ax3.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=7)

plt.tight_layout()
plt.show()

   
