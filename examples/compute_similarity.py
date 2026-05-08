import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("./features/global_features.csv")

X = df.drop(columns=["pdbid"]).values
sim = cosine_similarity(X)

print(sim.shape)
