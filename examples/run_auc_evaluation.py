import pandas as pd
from sklearn.metrics import roc_auc_score

df = pd.read_csv("similarity_scores.csv")

auc = roc_auc_score(df["label"], df["score"])
print("AUC:", auc)
