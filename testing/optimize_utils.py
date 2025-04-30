import numpy as np
import pandas as pd
from geopy.distance import geodesic
from sklearn.cluster import KMeans
import folium

def optimize_kmeans(df: pd.DataFrame, n_clusters: int) -> np.ndarray:
    coords = df[['latitude', 'longitude']].values
    model = KMeans(n_clusters=n_clusters, random_state=42).fit(coords)
    df['cluster'] = model.labels_
    centroids = model.cluster_centers_

    # Choose closest real zip to each centroid
    selected_indices = []
    for center in centroids:
        distances = np.linalg.norm(coords - center, axis=1)
        selected_indices.append(distances.argmin())
    return np.array(selected_indices)

def make_map(df: pd.DataFrame, list_selected_indices: list[tuple[np.ndarray, str, str]]) -> folium.Map:
    """
    Inputs:
        df: DataFrame of ZIP data
        list_selected_indices: list of tuples (indices_array, color, label)
    """
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=8)

    # Layer for all ZIPs
    base = folium.FeatureGroup(name="All ZIPs", show=True)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=3,
            color='gray',
            fill=True,
            fill_opacity=0.4
        ).add_to(base)
    base.add_to(m)

    # Layers for each optimization strategy
    for indices, color, label in list_selected_indices:
        layer = folium.FeatureGroup(name=label, show=True)
        for idx in indices:
            row = df.iloc[idx]
            folium.Marker(
                location=(row['latitude'], row['longitude']),
                popup=f"{label}<br>ZIP: {row['zip']}",
                icon=folium.Icon(color=color, icon='cutlery', prefix='fa')
            ).add_to(layer)
        layer.add_to(m)

    folium.LayerControl().add_to(m)
    return m

def optimize_greedy_coverage(D, optimizer, n_pantries, radius):
    covered = np.zeros(len(optimizer), dtype=bool)
    selected = []

    for _ in range(n_pantries):
        best_gain = 0
        best_idx = -1
        for i in range(len(optimizer)):
            if i in selected: 
                continue
            can_cover = (D[i] <= radius) & ~covered
            gain = optimizer[can_cover].sum()
            if gain > best_gain:
                best_gain, best_idx = gain, i
        selected.append(best_idx)
        covered |= (D[best_idx] <= radius)
    return np.array(selected)

def compute_distance_matrix(df: pd.DataFrame) -> np.ndarray:
    coords = list(zip(df['latitude'], df['longitude']))
    n = len(coords)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = geodesic(coords[i], coords[j]).miles
    return D