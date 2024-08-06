import pandas as pd
import networkx as nx
from sklearn.neighbors import NearestNeighbors
import numpy as np
from tqdm import tqdm
import pickle

def create_graph(csv_file, output_pickle, k=5):
    # load the dataset
    df = pd.read_csv(csv_file)
    print(df.head())

    # create a k-NN graph
    coords = df[['LATITUDE', 'LONGITUDE']].values
    nn = NearestNeighbors(n_neighbors=k+1, metric='haversine', n_jobs=-1)
    nn.fit(np.radians(coords))
    distances, indices = nn.kneighbors()

    # convert distances from radians to meters
    distances = distances * 6371000  # this is just earths radius

    # Create the graph
    G = nx.Graph()