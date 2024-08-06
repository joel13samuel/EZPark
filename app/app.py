from flask import Flask, render_template, request
import pandas as pd
import networkx as nx
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pickle
import folium
from geopy.distance import geodesic
import time

app = Flask(__name__)

# load the graph
def load_graph(pickle_file):
    with open(pickle_file, 'rb') as f:
        return pickle.load(f)

G = load_graph('parking_violations_graph.pickle')

# load the original data
data = pd.read_csv('cleaned_parking_violations.csv')

def find_nearest_node(lat, lon):
    coords = np.array([data['pos'] for _, data in G.nodes(data=True)])
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(coords)
    _, indices = nbrs.kneighbors([[lat, lon]])
    nearest_node = list(G.nodes())[indices[0][0]]
    return nearest_node

def bfs_violations(start_node, max_distance=500):
    visited = set()
    queue = [(start_node, 0)]
    violations = []

    while queue:
        node, distance = queue.pop(0)
        if node not in visited and distance <= max_distance:
            visited.add(node)
            violations.append(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    new_distance = distance + G[node][neighbor]['weight']
                    queue.append((neighbor, new_distance))

    return violations

def dijkstra_violations(start_node, max_distance=500):
    distances = {node: float('infinity') for node in G.nodes()}
    distances[start_node] = 0
    violations = []

    pq = [(0, start_node)]
    while pq:
        current_distance, current_node = min(pq)
        pq.remove((current_distance, current_node))

        if current_distance > max_distance:
            break

        violations.append(current_node)

        for neighbor in G.neighbors(current_node):
            distance = current_distance + G[current_node][neighbor]['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.append((distance, neighbor))

    return violations