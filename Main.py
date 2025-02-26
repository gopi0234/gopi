import folium
import pandas as pd

# Filter only Indian restaurants (assuming 'Country Code' column exists)
df_india = df[df["Country Code"] == 1]  # Change if your dataset uses a different code for India

# Ensure only rated restaurants are considered
df_india = df_india[df_india["Aggregate rating"] > 0]

# Get top 20 restaurants in each category
high_rated = df_india[df_india["Aggregate rating"] >= 4.0].nlargest(20, "Aggregate rating")
medium_rated = df_india[(df_india["Aggregate rating"] >= 2.5) & (df_india["Aggregate rating"] < 4.0)].nlargest(20, "Aggregate rating")
low_rated = df_india[df_india["Aggregate rating"] < 2.5].nlargest(20, "Aggregate rating")

# Merge top 20 from each category
top_restaurants = pd.concat([high_rated, medium_rated, low_rated])

# Calculate map center (average latitude and longitude)
map_center = [df_india["Latitude"].mean(), df_india["Longitude"].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=5)  # Zoomed out to cover India

# Function to assign colors based on rating
def rating_color(rating):
    if rating >= 4.0:
        return "green"  # High-rated
    elif rating >= 2.5:
        return "yellow"  # Medium-rated
    else:
        return "red"  # Low-rated

# Add markers for top restaurants
for _, row in top_restaurants.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Restaurant Name']} - Rating: {row['Aggregate rating']}",
        icon=folium.Icon(color=rating_color(row["Aggregate rating"]))
    ).add_to(restaurant_map)

# Show the map
restaurant_map
