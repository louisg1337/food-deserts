import pandas as pd
import numpy as np
from optimize_utils import compute_distance_matrix, optimize_kmeans, optimize_greedy_coverage, make_map
import folium

sample_data = pd.DataFrame({
    'zip': [1001, 1002, 1003],
    'latitude': [42.1, 42.2, 42.3],
    'longitude': [-72.1, -72.2, -72.3],
    'irs_estimated_population': [1000, 2000, 1500]
})

def test_distance_matrix():
    D = compute_distance_matrix(sample_data)
    assert D.shape == (3, 3)
    assert np.allclose(np.diag(D), 0.0)
    assert np.allclose(D, D.T)

def test_kmeans_output():
    selected = optimize_kmeans(sample_data, n_clusters=2)
    assert len(selected) == 2
    assert all(isinstance(i, (int, np.integer)) for i in selected)

def test_greedy_output():
    D = compute_distance_matrix(sample_data)
    pops = sample_data['irs_estimated_population'].values
    selected = optimize_greedy_coverage(D, pops, n_pantries=2, radius=10)
    assert len(selected) == 2
    assert len(set(selected)) == len(selected)

def test_map_generation():
    selected = np.array([0, 1])
    m = make_map(sample_data, [(selected, 'red', 'Test Layer')])
    assert isinstance(m, folium.Map)

